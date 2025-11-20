"""
Script de demonstração do Sistema de Cadastro
Este script demonstra as funcionalidades do sistema de forma automatizada
"""
from trabalho_oo import Pessoa, SistemaCadastro

def demo():
    print("="*60)
    print("DEMONSTRAÇÃO DO SISTEMA DE CADASTRO E IMPRESSÃO")
    print("="*60)
    print()
    
    # Criar sistema
    print("1. Criando o sistema de cadastro...")
    sistema = SistemaCadastro()
    print(f"   ✓ Sistema criado. Total de registros: {sistema.total_cadastrados()}")
    print()
    
    # Cadastrar pessoas
    print("2. Cadastrando pessoas no sistema...")
    pessoas = [
        Pessoa("Ana Silva", 28, "ana.silva@email.com"),
        Pessoa("Bruno Costa", 35, "bruno.costa@email.com"),
        Pessoa("Carla Souza", 22, "carla.souza@email.com"),
        Pessoa("Daniel Santos", 41, "daniel.santos@email.com"),
        Pessoa("Elena Ferreira", 19, "elena.ferreira@email.com")
    ]
    
    for pessoa in pessoas:
        sistema.cadastrar(pessoa)
    
    print()
    
    # Verificar total
    print(f"3. Total de pessoas cadastradas: {sistema.total_cadastrados()}")
    print()
    
    # Imprimir todas as pessoas
    print("4. Imprimindo todas as pessoas cadastradas:")
    sistema.imprimir()
    print()
    
    # Imprimir pessoa específica
    print("5. Imprimindo pessoa específica (índice 2):")
    sistema.imprimir_por_indice(2)
    print()
    
    # Teste de imprimir lista vazia
    print("6. Testando sistema vazio:")
    sistema_vazio = SistemaCadastro()
    sistema_vazio.imprimir()
    print()
    
    print("="*60)
    print("DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*60)
    print()
    print("Para usar o sistema interativo, execute:")
    print("  python3 trabalho_oo.py")

if __name__ == "__main__":
    demo()
