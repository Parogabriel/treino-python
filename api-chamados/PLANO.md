# Plano de trabalho

Uma sessão de 40 a 60 minutos por dia. Se uma etapa levar mais tempo, continue no dia seguinte. Faça commit quando uma mudança funcionar e você conseguir explicar o código.

O primeiro dia é o início do projeto; os demais dias são trabalho planejado. As mensagens abaixo são sugestões para usar depois de implementar e conferir cada mudança.

| Dia | O que fazer | Como conferir | Sugestão de commit |
| --- | --- | --- | --- |
| 1 | Subir o servidor e criar `/health` | Receber 200 e JSON; conferir o 404 | `adiciona rota para conferir o servidor` |
| 2 | Criar `POST /chamados`, ainda em memória | Enviar título e descrição; receber 201 e um id | `adiciona cadastro de chamados` |
| 3 | Limitar título e descrição | Aceitar textos no limite e retornar 400 quando passar | `limita o tamanho dos campos do chamado` |
| 4 | Salvar os chamados no SQLite, usando parâmetros no SQL | Reiniciar o servidor e manter os registros | `salva chamados no sqlite` |
| 5 | Listar e buscar por id | Listagem vazia funciona; id ausente retorna 404 | `adiciona consulta de chamados` |
| 6 | Alterar status: aberto, em atendimento e resolvido | Recusar status desconhecido; id ausente retorna 404 | `permite alterar o status do chamado` |
| 7 | Adicionar prioridade e filtro por status | Conferir filtros com e sem resultados | `adiciona prioridade e filtro por status` |
| 8 | Limitar o tamanho do corpo e paginar a listagem | Corpo muito grande retorna 413; página inválida retorna 400 | `limita os dados recebidos e a listagem` |
| 9 | Conferir o fluxo inteiro com testes HTTP | Cadastrar, consultar, alterar e consultar novamente em banco temporário | `testa o fluxo dos chamados` |
| 10 | Atualizar o README com exemplos reais de cada rota | Seguir as instruções em uma pasta nova | `documenta as rotas dos chamados` |

Antes de encerrar cada sessão:

1. Rodar os testes e conferir a resposta da rota que mudou.
2. Ler o diff e remover arquivos temporários, banco local e dados pessoais.
3. Fazer um commit só com a mudança concluída; separar uma correção independente se necessário.
4. Anotar em uma frase o que falta e o que você aprendeu.

Para explicar o projeto numa entrevista, pratique: o que é uma requisição HTTP, por que usar cada status, como o JSON vira bytes e como os registros continuam existindo depois de reiniciar o programa.

Não usar dados de clientes nem configurações reais do trabalho. Os exemplos devem ser fictícios. Autenticação e uso por vários usuários ficam para uma etapa posterior; esta versão é local.

## Andamento

- 09/11/2026: servidor local com `/health` e resposta 404 em JSON.
- 10/11/2026: cadastro de chamados em memória, com ID e validação básica dos campos. Testes para cadastro, dados inválidos e IDs em requisições simultâneas.
- 12/11/2026: limites para título e descrição, com testes para valores no limite e acima dele.
- 12/11/2026: cadastro salvo no SQLite e teste de reinício do servidor.
- 14/11/2026: listagem e busca por ID, com testes para banco vazio, ID ausente e consulta após reinício.
- Próxima sessão: alterar o status de um chamado.
