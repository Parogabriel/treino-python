# API de chamados

Projeto de estudo de back-end em Python para organizar chamados de suporte de internet.

Já é possível conferir se o servidor está funcionando e cadastrar chamados. Os dados ficam em memória e são apagados ao reiniciar o programa. A consulta dos chamados ainda não foi implementada.

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

A resposta tem status 201 e o chamado cadastrado:

```json
{"id": 1, "titulo": "Sem internet", "descricao": "Roteador sem sinal"}
```

O ID aumenta a cada cadastro e volta a 1 quando o programa é reiniciado. Título e descrição precisam ser textos não vazios. Após remover espaços nas pontas, o título aceita até 120 caracteres e a descrição até 2.000. JSON inválido, campos ausentes e textos acima dos limites retornam 400.

## Testar

```bash
python -m unittest discover -s tests -v
```

## Próximos passos

- Salvar e consultar os chamados no SQLite.
- Alterar o status de um chamado.
- Filtrar por status e prioridade.

O plano de trabalho está em [PLANO.md](PLANO.md).
