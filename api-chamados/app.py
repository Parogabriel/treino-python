import json
import sqlite3
from contextlib import closing
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

STATUS_VALIDOS = ('aberto', 'em atendimento', 'resolvido')


class Servidor(ThreadingHTTPServer):
    def __init__(self, endereco, banco=Path(__file__).with_name('chamados.db')):
        self.banco = banco
        with closing(sqlite3.connect(banco)) as conexao:
            conexao.execute('BEGIN IMMEDIATE')
            conexao.execute('''CREATE TABLE IF NOT EXISTS chamados (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'aberto'
            )''')
            colunas = [coluna[1] for coluna in conexao.execute('PRAGMA table_info(chamados)')]
            if 'status' not in colunas:
                conexao.execute("ALTER TABLE chamados ADD COLUMN status TEXT NOT NULL DEFAULT 'aberto'")
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

    def consultar_chamados(self, chamado_id=None):
        with closing(sqlite3.connect(self.banco)) as conexao:
            conexao.row_factory = sqlite3.Row
            if chamado_id is None:
                linhas = conexao.execute('SELECT id, titulo, descricao, status FROM chamados ORDER BY id')
            else:
                linhas = conexao.execute(
                    'SELECT id, titulo, descricao, status FROM chamados WHERE id = ?', (chamado_id,),
                )
            return [dict(linha) for linha in linhas]

    def atualizar_status(self, chamado_id, status):
        with closing(sqlite3.connect(self.banco)) as conexao:
            conexao.row_factory = sqlite3.Row
            cursor = conexao.execute('UPDATE chamados SET status = ? WHERE id = ?', (status, chamado_id))
            if cursor.rowcount == 0:
                return None
            chamado = conexao.execute(
                'SELECT id, titulo, descricao, status FROM chamados WHERE id = ?', (chamado_id,),
            ).fetchone()
            conexao.commit()
            return dict(chamado)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        caminho = urlsplit(self.path).path
        if caminho == '/health':
            self.responder(200, {'status': 'ok'})
            return

        prefixo, _, chamado_id = caminho.rpartition('/')
        lista = caminho == '/chamados'
        if not lista and not (prefixo == '/chamados' and chamado_id.isascii() and chamado_id.isdecimal()):
            self.responder(404, {'erro': 'Rota não encontrada'})
            return

        try:
            chamados = self.server.consultar_chamados(None if lista else chamado_id)
        except sqlite3.Error as erro:
            self.log_error('Erro ao consultar chamados: %s', erro)
            self.responder(500, {'erro': 'Não foi possível consultar os chamados'})
            return

        if lista:
            self.responder(200, chamados)
        elif chamados:
            self.responder(200, chamados[0])
        else:
            self.responder(404, {'erro': 'Chamado não encontrado'})

    def do_POST(self):
        if urlsplit(self.path).path != '/chamados':
            self.responder(404, {'erro': 'Rota não encontrada'})
            return

        try:
            dados = self.ler_json()
        except ValueError:
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
        self.responder(201, {'id': chamado_id, 'titulo': titulo, 'descricao': descricao, 'status': 'aberto'})

    def do_PATCH(self):
        caminho = urlsplit(self.path).path
        prefixo, _, chamado_id = caminho.rpartition('/')
        if prefixo != '/chamados' or not (chamado_id.isascii() and chamado_id.isdecimal()):
            self.responder(404, {'erro': 'Rota não encontrada'})
            return

        try:
            dados = self.ler_json()
        except ValueError:
            self.responder(400, {'erro': 'Envie um corpo JSON válido'})
            return

        status = dados.get('status') if isinstance(dados, dict) else None
        if status not in STATUS_VALIDOS:
            self.responder(400, {'erro': 'Status deve ser aberto, em atendimento ou resolvido'})
            return

        try:
            chamado = self.server.atualizar_status(chamado_id, status)
        except sqlite3.Error as erro:
            self.log_error('Erro ao atualizar status: %s', erro)
            self.responder(500, {'erro': 'Não foi possível atualizar o status do chamado'})
            return

        if chamado is None:
            self.responder(404, {'erro': 'Chamado não encontrado'})
        else:
            self.responder(200, chamado)

    def ler_json(self):
        tamanho = int(self.headers.get('Content-Length', '0'))
        if tamanho <= 0:
            raise ValueError
        return json.loads(self.rfile.read(tamanho))

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
