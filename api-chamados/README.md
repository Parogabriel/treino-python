# API de chamados

Projeto de estudo de back-end em Python para organizar chamados de suporte de internet.

Por enquanto, só existe uma rota para conferir se o servidor está funcionando. O cadastro e o acompanhamento dos chamados serão os próximos passos.

## Rodar

Python 3.10 ou mais recente. Não precisa instalar pacotes.

Na pasta `api-chamados`:

```bash
python app.py
```

Abra http://127.0.0.1:8000/health no navegador. A resposta deve ser:

```json
{"status": "ok"}
```

Outros caminhos retornam 404 em JSON. O servidor só aceita conexões locais e serve para estudo.

## Testar

```bash
python -m unittest discover -s tests -v
```

## Próximos passos

- Cadastrar chamados com título e descrição.
- Salvar e consultar os chamados no SQLite.
- Alterar o status de um chamado.
- Filtrar por status e prioridade.

O plano de trabalho está em [PLANO.md](PLANO.md).
