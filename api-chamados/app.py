import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path == '/health':
            self.responder(200, {'status': 'ok'})
        else:
            self.responder(404, {'erro': 'Rota não encontrada'})

    def responder(self, status, dados):
        corpo = json.dumps(dados, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)


if __name__ == '__main__':
    servidor = ThreadingHTTPServer(('127.0.0.1', 8000), Handler)
    print('Servidor em http://127.0.0.1:8000')
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        servidor.server_close()
