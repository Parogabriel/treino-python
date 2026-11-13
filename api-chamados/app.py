import json
import sqlite3
from contextlib import closing
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


class Servidor(ThreadingHTTPServer):
    def __init__(self, endereco, banco=Path(__file__).with_name('chamados.db')):
        self.banco = banco
        with closing(sqlite3.connect(banco)) as conexao:
            conexao.execute('''CREATE TABLE IF NOT EXISTS chamados (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL
            )''')
            conexao.commit()
        super().__init__(endereco, Handler)

    def salvar_chamado(self, titulo, descricao):
        with closing(sqlite3.connect(self.banco)) as conexao:
            cursor = conexao.execute(
                'INSERT INTO chamados (titulo, descricao) VALUES (?, ?)',
                (titulo, descricao),
            )
            conexao.commit()
            return cursor.lastrowid


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

        titulo = dados['titulo'].strip()
        descricao = dados['descricao'].strip()
        if len(titulo) > 120 or len(descricao) > 2000:
            self.responder(400, {'erro': 'O título aceita até 120 caracteres e a descrição até 2000'})
            return

        try:
            chamado_id = self.server.salvar_chamado(titulo, descricao)
        except sqlite3.Error as erro:
            self.log_error('Erro ao salvar chamado: %s', erro)
            self.responder(500, {'erro': 'Não foi possível salvar o chamado'})
            return
        self.responder(201, {'id': chamado_id, 'titulo': titulo, 'descricao': descricao})

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
