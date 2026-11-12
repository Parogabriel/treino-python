import json
import threading
import unittest
from http.client import HTTPConnection
from concurrent.futures import ThreadPoolExecutor

from app import Servidor


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.servidor = Servidor(('127.0.0.1', 0))
        cls.thread = threading.Thread(target=cls.servidor.serve_forever)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.servidor.shutdown()
        cls.servidor.server_close()
        cls.thread.join()

    def setUp(self):
        self.servidor.chamados.clear()

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
        self.assertEqual(self.consultar('/chamados'), (404, {'erro': 'Rota não encontrada'}))

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
        self.assertEqual(self.servidor.chamados, [chamado])

    def test_cadastros_simultaneos_recebem_ids_diferentes(self):
        with ThreadPoolExecutor(max_workers=4) as pool:
            respostas = list(pool.map(self.cadastrar, [
                {'titulo': f'Chamado {i}', 'descricao': 'Sem internet.'}
                for i in range(8)
            ]))
        self.assertTrue(all(status == 201 for status, _ in respostas))
        self.assertEqual(sorted(item['id'] for _, item in respostas), list(range(1, 9)))
        self.assertEqual(len(self.servidor.chamados), 8)

    def test_rejeita_campos_invalidos_sem_salvar(self):
        for dados in [None, [], {}, {'titulo': 'Sem internet'},
                      {'titulo': ' ', 'descricao': 'Sem sinal'},
                      {'titulo': 'Sem internet', 'descricao': 12}]:
            with self.subTest(dados=dados):
                self.assertEqual(self.cadastrar(dados)[0], 400)
        self.assertEqual(self.servidor.chamados, [])

    def test_rejeita_json_invalido(self):
        for corpo in [b'', b'{', b'\xff']:
            with self.subTest(corpo=corpo):
                self.assertEqual(self.consultar('/chamados', 'POST', corpo)[0], 400)
        self.assertEqual(self.servidor.chamados, [])

    def test_rejeita_textos_acima_do_limite(self):
        for dados in (
            {'titulo': 'a' * 121, 'descricao': 'Sem sinal'},
            {'titulo': 'Sem internet', 'descricao': 'a' * 2001},
        ):
            with self.subTest(campo='titulo' if len(dados['titulo']) > 120 else 'descricao'):
                self.assertEqual(self.cadastrar(dados)[0], 400)
        self.assertEqual(self.servidor.chamados, [])

    def test_aceita_textos_no_limite_depois_de_remover_espacos(self):
        status, chamado = self.cadastrar({'titulo': ' ' + 'é' * 120, 'descricao': 'a' * 2000 + ' '})
        self.assertEqual(status, 201)
        self.assertEqual(chamado['titulo'], 'é' * 120)
        self.assertEqual(chamado['descricao'], 'a' * 2000)

    def test_post_em_rota_inexistente(self):
        self.assertEqual(self.consultar('/outra-rota', 'POST')[0], 404)

    def test_servidor_novo_comeca_sem_chamados(self):
        self.cadastrar({'titulo': 'Teste', 'descricao': 'Sem conexão'})
        outro = Servidor(('127.0.0.1', 0))
        try:
            self.assertEqual(outro.chamados, [])
        finally:
            outro.server_close()


if __name__ == '__main__':
    unittest.main()
