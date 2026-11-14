import json
import sqlite3
import tempfile
import threading
import unittest
from contextlib import ExitStack, closing, contextmanager
from http.client import HTTPConnection
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from app import Servidor


@contextmanager
def servidor_rodando(banco):
    with Servidor(('127.0.0.1', 0), banco) as servidor:
        thread = threading.Thread(target=servidor.serve_forever, kwargs={'poll_interval': 0.02})
        thread.start()
        try:
            yield servidor
        finally:
            servidor.shutdown()
            thread.join()


class ApiTests(unittest.TestCase):
    def setUp(self):
        pasta = tempfile.TemporaryDirectory()
        self.addCleanup(pasta.cleanup)
        self.banco = Path(pasta.name) / 'teste.db'
        self.sessao = ExitStack()
        self.addCleanup(self.sessao.close)
        self.servidor = self.sessao.enter_context(servidor_rodando(self.banco))

    def registros(self):
        with closing(sqlite3.connect(self.banco)) as conexao:
            return conexao.execute('SELECT id, titulo, descricao FROM chamados ORDER BY id').fetchall()

    def consultar(self, caminho, metodo='GET', corpo=None):
        conexao = HTTPConnection(*self.servidor.server_address, timeout=3)
        try:
            conexao.request(metodo, caminho, body=corpo,
                            headers={'Content-Type': 'application/json'})
            resposta = conexao.getresponse()
            corpo = resposta.read()
            self.assertEqual(int(resposta.getheader('Content-Length')), len(corpo))
            self.assertEqual(resposta.getheader('Content-Type'), 'application/json; charset=utf-8')
            return resposta.status, json.loads(corpo)
        finally:
            conexao.close()

    def test_health(self):
        self.assertEqual(self.consultar('/health'), (200, {'status': 'ok'}))

    def test_health_com_parametro(self):
        self.assertEqual(self.consultar('/health?check=1')[0], 200)

    def test_rota_inexistente(self):
        for caminho in ('/outra-rota', '/chamados/abc', '/chamados/1/outro'):
            with self.subTest(caminho=caminho):
                self.assertEqual(self.consultar(caminho), (404, {'erro': 'Rota não encontrada'}))

    def test_lista_vazia(self):
        self.assertEqual(self.consultar('/chamados'), (200, []))

    def test_lista_chamados_na_ordem_de_cadastro(self):
        _, primeiro = self.cadastrar({'titulo': 'Sem internet', 'descricao': 'Sem sinal'})
        _, segundo = self.cadastrar({'titulo': 'Conexão lenta', 'descricao': 'Sinal fraco'})
        self.assertEqual(self.consultar('/chamados'), (200, [primeiro, segundo]))

    def test_busca_chamado_por_id(self):
        _, chamado = self.cadastrar({'titulo': 'Falha', 'descricao': 'Sem conexão'})
        self.assertEqual(self.consultar(f'/chamados/{chamado["id"]}'), (200, chamado))

    def test_busca_id_inexistente(self):
        self.assertEqual(self.consultar('/chamados/999'), (404, {'erro': 'Chamado não encontrado'}))

    def cadastrar(self, dados):
        return self.consultar('/chamados', 'POST', json.dumps(dados).encode('utf-8'))

    def test_cadastra_e_guarda_o_chamado(self):
        status, chamado = self.cadastrar({
            'titulo': ' Sem conexão ', 'descricao': ' Roteador sem sinal. ',
        })
        self.assertEqual(status, 201)
        self.assertEqual(chamado, {
            'id': 1, 'titulo': 'Sem conexão', 'descricao': 'Roteador sem sinal.',
        })
        self.assertEqual(self.registros(), [(1, 'Sem conexão', 'Roteador sem sinal.')])

    def test_cadastros_simultaneos_recebem_ids_diferentes(self):
        with ThreadPoolExecutor(max_workers=4) as pool:
            respostas = list(pool.map(self.cadastrar, [
                {'titulo': f'Chamado {i}', 'descricao': 'Sem internet.'}
                for i in range(8)
            ]))
        self.assertTrue(all(status == 201 for status, _ in respostas))
        self.assertEqual(sorted(item['id'] for _, item in respostas), list(range(1, 9)))
        self.assertEqual(len(self.registros()), 8)

    def test_rejeita_campos_invalidos_sem_salvar(self):
        for dados in [None, [], {}, {'titulo': 'Sem internet'},
                      {'titulo': ' ', 'descricao': 'Sem sinal'},
                      {'titulo': 'Sem internet', 'descricao': 12}]:
            with self.subTest(dados=dados):
                self.assertEqual(self.cadastrar(dados)[0], 400)
        self.assertEqual(self.registros(), [])

    def test_rejeita_json_invalido(self):
        for corpo in [b'', b'{', b'\xff']:
            with self.subTest(corpo=corpo):
                self.assertEqual(self.consultar('/chamados', 'POST', corpo)[0], 400)
        self.assertEqual(self.registros(), [])

    def test_rejeita_textos_acima_do_limite(self):
        for dados in (
            {'titulo': 'a' * 121, 'descricao': 'Sem sinal'},
            {'titulo': 'Sem internet', 'descricao': 'a' * 2001},
        ):
            with self.subTest(campo='titulo' if len(dados['titulo']) > 120 else 'descricao'):
                self.assertEqual(self.cadastrar(dados)[0], 400)
        self.assertEqual(self.registros(), [])

    def test_aceita_textos_no_limite_depois_de_remover_espacos(self):
        status, chamado = self.cadastrar({'titulo': ' ' + 'é' * 120, 'descricao': 'a' * 2000 + ' '})
        self.assertEqual(status, 201)
        self.assertEqual(chamado['titulo'], 'é' * 120)
        self.assertEqual(chamado['descricao'], 'a' * 2000)

    def test_post_em_rota_inexistente(self):
        self.assertEqual(self.consultar('/outra-rota', 'POST')[0], 404)

    def test_chamados_permanecem_depois_de_reiniciar(self):
        status, primeiro = self.cadastrar({'titulo': "Cabo d'água", 'descricao': 'Sem conexão'})
        self.assertEqual(status, 201)
        self.sessao.close()

        self.servidor = self.sessao.enter_context(servidor_rodando(self.banco))
        self.assertEqual(self.consultar(f'/chamados/{primeiro["id"]}'), (200, primeiro))
        status, segundo = self.cadastrar({'titulo': 'Novo chamado', 'descricao': 'Sem sinal'})
        self.assertEqual(status, 201)
        self.assertEqual(segundo['id'], primeiro['id'] + 1)
        self.assertEqual(self.registros(), [
            (primeiro['id'], "Cabo d'água", 'Sem conexão'),
            (segundo['id'], 'Novo chamado', 'Sem sinal'),
        ])


if __name__ == '__main__':
    unittest.main()
