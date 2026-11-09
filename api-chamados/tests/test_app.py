import json
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer

from app import Handler


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.servidor = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.servidor.serve_forever)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.servidor.shutdown()
        cls.servidor.server_close()
        cls.thread.join()

    def consultar(self, caminho):
        conexao = HTTPConnection(*self.servidor.server_address, timeout=3)
        try:
            conexao.request('GET', caminho)
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


if __name__ == '__main__':
    unittest.main()
