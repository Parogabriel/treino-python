# Sistema de Cadastro - Trabalho de Python OO

Este projeto implementa um sistema de cadastro e impressão (cadastrar e imprimir) usando Programação Orientada a Objetos em Python.

## Descrição

O sistema permite:
- **Cadastrar** pessoas com nome, idade e email
- **Imprimir** a lista completa de pessoas cadastradas
- **Visualizar** o total de cadastros realizados
- Interface interativa via menu

## Como Executar

Para executar o sistema interativo:

```bash
python3 trabalho_oo.py
```

## Estrutura do Código

### Classes

#### `Pessoa`
Representa uma pessoa com os seguintes atributos:
- `nome`: Nome da pessoa
- `idade`: Idade da pessoa
- `email`: Email da pessoa

#### `SistemaCadastro`
Gerencia o cadastro e impressão de pessoas:
- `cadastrar(pessoa)`: Adiciona uma nova pessoa ao sistema
- `imprimir()`: Exibe todas as pessoas cadastradas
- `imprimir_por_indice(indice)`: Exibe uma pessoa específica
- `total_cadastrados()`: Retorna o número total de pessoas cadastradas

## Exemplo de Uso

```python
from trabalho_oo import Pessoa, SistemaCadastro

# Criar sistema
sistema = SistemaCadastro()

# Cadastrar pessoas
pessoa1 = Pessoa("João Silva", 25, "joao@email.com")
pessoa2 = Pessoa("Maria Santos", 30, "maria@email.com")

sistema.cadastrar(pessoa1)
sistema.cadastrar(pessoa2)

# Imprimir pessoas cadastradas
sistema.imprimir()

# Ver total
print(f"Total: {sistema.total_cadastrados()}")
```

## Menu Interativo

O programa oferece um menu com as seguintes opções:

1. **Cadastrar pessoa** - Adiciona uma nova pessoa ao sistema
2. **Imprimir todas as pessoas** - Mostra lista completa
3. **Ver total de cadastros** - Exibe quantidade de registros
0. **Sair** - Encerra o programa

## Requisitos

- Python 3.6 ou superior

## Autor

Desenvolvido como trabalho de Programação Orientada a Objetos em Python.
