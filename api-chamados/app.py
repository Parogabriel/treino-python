import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock
from urllib.parse import urlsplit


class Servidor(ThreadingHTTPServer):
    def __init__(self, endereco):
        super().__init__(endereco, Handler)
        self.chamados = []
        self.lock = Lock()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path == '/health':
            self.responder(200, {'status': 'ok'})
        else:
            self.responder(404, {'erro': 'Rota não encontrada'})

    def do_POST(self):
        if urlsplit(self.path).path != '/chamados':
            self.responder(404, {'erro': 'Rota não encontrada'})
            return

        try:
            tamanho = int(self.headers.get('Content-Length', '0'))
            if tamanho <= 0:
                raise ValueError
            dados = json.loads(self.rfile.read(tamanho))
        except (ValueError, UnicodeDecodeError):
            self.responder(400, {'erro': 'Envie um corpo JSON válido'})
            return

        campos = ('titulo', 'descricao')
        if not isinstance(dados, dict) or not all(
            isinstance(dados.get(campo), str) and dados[campo].strip()
            for campo in campos
        ):
            self.responder(400, {'erro': 'Informe título e descrição como textos não vazios'})
            return

        with self.server.lock:
            chamado = {
                'id': len(self.server.chamados) + 1,
                'titulo': dados['titulo'].strip(),
                'descricao': dados['descricao'].strip(),
            }
            self.server.chamados.append(chamado)
        self.responder(201, chamado)

    def responder(self, status, dados):
        corpo = json.dumps(dados, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)


if __name__ == '__main__':
    servidor = Servidor(('127.0.0.1', 8000))
    print('Servidor em http://127.0.0.1:8000')
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        servidor.server_close()
