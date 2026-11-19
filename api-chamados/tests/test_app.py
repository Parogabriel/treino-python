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
            'status': 'aberto',
            'prioridade': 'normal',
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

    def test_atualiza_status_e_mantem_apos_reiniciar(self):
        _, chamado = self.cadastrar({'titulo': 'Falha', 'descricao': 'Sem conexão'})
        caminho = f'/chamados/{chamado["id"]}'
        for status in ('em atendimento', 'resolvido', 'aberto', 'resolvido'):
            resposta = self.consultar(caminho, 'PATCH', json.dumps({'status': status}))
            self.assertEqual(resposta, (200, {**chamado, 'status': status}))
        self.sessao.close()
        self.servidor = self.sessao.enter_context(servidor_rodando(self.banco))
        atualizado = {**chamado, 'status': 'resolvido'}
        self.assertEqual(self.consultar(caminho), (200, atualizado))
        self.assertEqual(self.consultar('/chamados'), (200, [atualizado]))

    def test_rejeita_status_invalido_sem_alterar_chamado(self):
        _, chamado = self.cadastrar({'titulo': 'Falha', 'descricao': 'Sem conexão'})
        caminho = f'/chamados/{chamado["id"]}'
        for corpo in ('{}', '{', '[]', '{"status": "cancelado"}', '{"status": 1}'):
            with self.subTest(corpo=corpo):
                self.assertEqual(self.consultar(caminho, 'PATCH', corpo)[0], 400)
        self.assertEqual(self.consultar(caminho), (200, chamado))

    def test_atualiza_id_inexistente(self):
        resposta = self.consultar('/chamados/999', 'PATCH', '{"status": "resolvido"}')
        self.assertEqual(resposta, (404, {'erro': 'Chamado não encontrado'}))

    def test_preserva_chamados_do_banco_anterior(self):
        banco_antigo = self.banco.with_name('antigo.db')
        with closing(sqlite3.connect(banco_antigo)) as conexao:
            conexao.execute('CREATE TABLE chamados (id INTEGER PRIMARY KEY, titulo TEXT NOT NULL, descricao TEXT NOT NULL)')
            conexao.execute('INSERT INTO chamados VALUES (?, ?, ?)', (7, 'Falha', 'Sem sinal'))
            conexao.commit()
        with servidor_rodando(banco_antigo) as servidor:
            self.servidor = servidor
            self.assertEqual(self.consultar('/chamados/7'), (200, {
                'id': 7, 'titulo': 'Falha', 'descricao': 'Sem sinal', 'status': 'aberto',
                'prioridade': 'normal',
            }))

    def test_aceita_cada_prioridade(self):
        for prioridade in ('baixa', 'normal', 'alta'):
            with self.subTest(prioridade=prioridade):
                status, chamado = self.cadastrar({
                    'titulo': 'Falha', 'descricao': 'Sem sinal', 'prioridade': prioridade,
                })
                self.assertEqual(status, 201)
                self.assertEqual(chamado['prioridade'], prioridade)
                self.assertEqual(self.consultar(f'/chamados/{chamado["id"]}'), (200, chamado))

    def test_rejeita_prioridade_invalida_sem_salvar(self):
        for prioridade in ('urgente', '', None, 1, [], {}):
            with self.subTest(prioridade=prioridade):
                self.assertEqual(self.cadastrar({
                    'titulo': 'Falha', 'descricao': 'Sem sinal', 'prioridade': prioridade,
                })[0], 400)
        self.assertEqual(self.registros(), [])

    def test_filtra_por_cada_status(self):
        esperados = {}
        for status in ('aberto', 'em atendimento', 'resolvido'):
            _, chamado = self.cadastrar({'titulo': status, 'descricao': 'Teste do filtro'})
            if status != 'aberto':
                _, chamado = self.consultar(f'/chamados/{chamado["id"]}', 'PATCH', json.dumps({'status': status}))
            esperados[status] = chamado
        for status, chamado in esperados.items():
            with self.subTest(status=status):
                caminho = '/chamados?status=' + status.replace(' ', '%20')
                self.assertEqual(self.consultar(caminho), (200, [chamado]))
        self.assertEqual(self.consultar('/chamados'), (200, list(esperados.values())))

    def test_filtro_sem_resultado(self):
        self.cadastrar({'titulo': 'Falha', 'descricao': 'Sem sinal'})
        self.assertEqual(self.consultar('/chamados?status=resolvido'), (200, []))

    def test_rejeita_filtro_invalido(self):
        for filtro in ('status=', 'status=cancelado', 'status=aberto&status=resolvido'):
            with self.subTest(filtro=filtro):
                self.assertEqual(self.consultar('/chamados?' + filtro)[0], 400)

    def test_paginacao_padrao(self):
        chamados = []
        for numero in range(22):
            status, chamado = self.cadastrar({'titulo': f'Chamado {numero}', 'descricao': 'Sem sinal'})
            self.assertEqual(status, 201)
            chamados.append(chamado)
        self.assertEqual(self.consultar('/chamados'), (200, chamados[:20]))
        self.assertEqual(self.consultar('/chamados?pagina=2'), (200, chamados[20:]))
        self.assertEqual(self.consultar('/chamados?pagina=3'), (200, []))
        self.assertEqual(self.consultar('/chamados/22'), (200, chamados[-1]))

    def test_pagina_com_limite_e_filtro(self):
        abertos = []
        for numero in range(7):
            _, chamado = self.cadastrar({'titulo': f'Chamado {numero}', 'descricao': 'Sem sinal'})
            if numero % 2 == 0:
                self.consultar(f'/chamados/{chamado["id"]}', 'PATCH', '{"status": "resolvido"}')
            else:
                abertos.append(chamado)
        self.assertEqual(self.consultar('/chamados?status=aberto&limite=2'), (200, abertos[:2]))
        self.assertEqual(self.consultar('/chamados?status=aberto&limite=2&pagina=2'), (200, abertos[2:]))
        self.assertEqual(self.consultar('/chamados?status=aberto&limite=2&pagina=3'), (200, []))

    def test_rejeita_paginacao_invalida(self):
        for parametro in ('pagina', 'limite'):
            for valor in ('', '0', '-1', '1.5', 'abc', '%2B1', '%201', '%D9%A1', '999999999999999999999'):
                with self.subTest(parametro=parametro, valor=valor):
                    self.assertEqual(self.consultar(f'/chamados?{parametro}={valor}')[0], 400)
            with self.subTest(parametro=parametro, repetido=True):
                self.assertEqual(self.consultar(f'/chamados?{parametro}=1&{parametro}=2')[0], 400)
        for query in ('pagina=1000001', 'limite=101'):
            with self.subTest(query=query):
                self.assertEqual(self.consultar('/chamados?' + query)[0], 400)

    def test_aceita_extremos_da_paginacao(self):
        _, chamado = self.cadastrar({'titulo': 'Falha', 'descricao': 'Sem sinal'})
        self.assertEqual(self.consultar('/chamados?pagina=1&limite=1'), (200, [chamado]))
        self.assertEqual(self.consultar('/chamados?pagina=1&limite=100'), (200, [chamado]))
        self.assertEqual(self.consultar('/chamados?pagina=1000000&limite=100'), (200, []))

    def test_rejeita_cadastro_acima_de_32_kib_sem_salvar(self):
        corpo = b'{"titulo": "Falha", "descricao": "Sem sinal"}'.ljust(32769, b' ')
        status, resposta = self.consultar('/chamados', 'POST', corpo)
        self.assertEqual(status, 413)
        self.assertIn('erro', resposta)
        self.assertEqual(self.registros(), [])

    def test_rejeita_patch_acima_de_32_kib_sem_alterar(self):
        _, chamado = self.cadastrar({'titulo': 'Falha', 'descricao': 'Sem sinal'})
        caminho = f'/chamados/{chamado["id"]}'
        corpo = b'{"status": "resolvido"}'.ljust(32769, b' ')
        status, resposta = self.consultar(caminho, 'PATCH', corpo)
        self.assertEqual(status, 413)
        self.assertIn('erro', resposta)
        self.assertEqual(self.consultar(caminho), (200, chamado))

    def test_aceita_corpo_com_exatos_32_kib(self):
        corpo = json.dumps({'titulo': 'Conexão lenta', 'descricao': 'Sinal fraco'}, ensure_ascii=False)
        status, chamado = self.consultar('/chamados', 'POST', corpo.encode('utf-8').ljust(32768, b' '))
        self.assertEqual(status, 201)
        self.assertEqual(chamado['titulo'], 'Conexão lenta')
        caminho = f'/chamados/{chamado["id"]}'
        corpo = b'{"status": "resolvido"}'.ljust(32768, b' ')
        esperado = {**chamado, 'status': 'resolvido'}
        self.assertEqual(self.consultar(caminho, 'PATCH', corpo), (200, esperado))
        self.assertEqual(self.consultar(caminho), (200, esperado))

    def test_preserva_status_ao_migrar_prioridade(self):
        banco_antigo = self.banco.with_name('com-status.db')
        with closing(sqlite3.connect(banco_antigo)) as conexao:
            conexao.execute('CREATE TABLE chamados (id INTEGER PRIMARY KEY, titulo TEXT NOT NULL, descricao TEXT NOT NULL, status TEXT NOT NULL)')
            conexao.execute('INSERT INTO chamados VALUES (?, ?, ?, ?)', (8, 'Falha', 'Sem sinal', 'resolvido'))
            conexao.commit()
        with servidor_rodando(banco_antigo) as servidor:
            self.servidor = servidor
            self.assertEqual(self.consultar('/chamados/8'), (200, {
                'id': 8, 'titulo': 'Falha', 'descricao': 'Sem sinal',
                'status': 'resolvido', 'prioridade': 'normal',
            }))

    def test_prioridade_permanece_apos_patch_e_reinicio(self):
        _, chamado = self.cadastrar({'titulo': 'Falha', 'descricao': 'Sem sinal', 'prioridade': 'alta'})
        caminho = f'/chamados/{chamado["id"]}'
        esperado = {**chamado, 'status': 'resolvido'}
        self.assertEqual(self.consultar(caminho, 'PATCH', '{"status": "resolvido"}'), (200, esperado))
        self.sessao.close()
        self.servidor = self.sessao.enter_context(servidor_rodando(self.banco))
        self.assertEqual(self.consultar(caminho), (200, esperado))

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
