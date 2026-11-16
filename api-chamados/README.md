# API de chamados

Projeto de estudo de back-end em Python para organizar chamados de suporte de internet.

A API permite cadastrar, listar, consultar e atualizar o status dos chamados. O SQLite salva os dados em `chamados.db`, ao lado de `app.py`, e mantém os registros ao reiniciar o programa.

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

## Cadastrar um chamado

Envie `POST /chamados` com título e descrição em JSON. No PowerShell:

```powershell
$dados = @{ titulo = 'Sem internet'; descricao = 'Roteador sem sinal' } | ConvertTo-Json
Invoke-RestMethod -Uri http://127.0.0.1:8000/chamados -Method Post -ContentType 'application/json; charset=utf-8' -Body ([System.Text.Encoding]::UTF8.GetBytes($dados))
```

A resposta tem status 201 e o chamado cadastrado. Em um banco novo, o primeiro chamado tem ID 1:

```json
{"id": 1, "titulo": "Sem internet", "descricao": "Roteador sem sinal", "status": "aberto", "prioridade": "normal"}
```

O SQLite gera o ID e a numeração continua ao reiniciar. Título e descrição precisam ser textos não vazios. Após remover espaços nas pontas, o título aceita até 120 caracteres e a descrição até 2.000. JSON inválido, campos ausentes e textos acima dos limites retornam 400.

O campo opcional `prioridade` aceita `baixa`, `normal` ou `alta` no cadastro. Se ele não for enviado, o chamado recebe `normal`. Valores inválidos retornam `400`. A prioridade fica salva no SQLite e não muda ao atualizar o status.

## Consultar chamados

```powershell
Invoke-RestMethod http://127.0.0.1:8000/chamados
Invoke-RestMethod http://127.0.0.1:8000/chamados/1
```

`GET /chamados` retorna a lista em ordem de ID, ou `[]` se não houver registros. `GET /chamados/1` retorna o chamado de ID 1, ou `404` se ele não existir.

Para listar apenas os chamados de um status:

```powershell
Invoke-RestMethod 'http://127.0.0.1:8000/chamados?status=aberto'
Invoke-RestMethod 'http://127.0.0.1:8000/chamados?status=em%20atendimento'
```

O filtro aceita os mesmos status da atualização. Um status vazio, desconhecido ou repetido na URL retorna `400`. Se não houver chamados naquele status, a resposta é `[]`.

## Alterar o status

```powershell
$dados = @{ status = 'em atendimento' } | ConvertTo-Json
Invoke-RestMethod -Uri http://127.0.0.1:8000/chamados/1 -Method Patch -ContentType 'application/json' -Body $dados
```

`PATCH /chamados/1` retorna `200` com o chamado atualizado. Os valores aceitos são `aberto`, `em atendimento` e `resolvido`. Um status inválido retorna `400`; um ID que não existe retorna `404`.

Chamados novos começam como `aberto`. Ao iniciar com um banco de uma versão ainda sem a coluna de status, os registros existentes são mantidos e recebem o status `aberto`.

Ao migrar de uma versão sem prioridade, os chamados recebem prioridade `normal` e mantêm o status que já tinham.

## Testar

```bash
python -m unittest discover -s tests -v
```

## Próximos passos

- Limitar o tamanho das requisições e paginar a listagem.

O plano de trabalho está em [PLANO.md](PLANO.md).
