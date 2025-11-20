"""
Trabalho de Python - Programação Orientada a Objetos
Sistema de Cadastro e Impressão (Cadastrar e Imprimir)
"""


class Pessoa:
    """Classe base para representar uma pessoa"""
    
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"


class SistemaCadastro:
    """Sistema de cadastro e impressão de pessoas"""
    
    def __init__(self):
        self.pessoas = []
    
    def cadastrar(self, pessoa):
        """Cadastra uma nova pessoa no sistema"""
        self.pessoas.append(pessoa)
        print(f"\n✓ Pessoa cadastrada com sucesso!")
    
    def imprimir(self):
        """Imprime todas as pessoas cadastradas"""
        if not self.pessoas:
            print("\nNenhuma pessoa cadastrada ainda.")
            return
        
        print("\n" + "="*50)
        print("LISTA DE PESSOAS CADASTRADAS")
        print("="*50)
        for i, pessoa in enumerate(self.pessoas, 1):
            print(f"{i}. {pessoa}")
        print("="*50)
    
    def imprimir_por_indice(self, indice):
        """Imprime uma pessoa específica pelo índice"""
        if 0 <= indice < len(self.pessoas):
            print(f"\n{self.pessoas[indice]}")
        else:
            print("\nÍndice inválido!")
    
    def total_cadastrados(self):
        """Retorna o total de pessoas cadastradas"""
        return len(self.pessoas)


def menu():
    """Exibe o menu de opções"""
    print("\n" + "="*50)
    print("SISTEMA DE CADASTRO")
    print("="*50)
    print("1. Cadastrar pessoa")
    print("2. Imprimir todas as pessoas")
    print("3. Ver total de cadastros")
    print("0. Sair")
    print("="*50)


def main():
    """Função principal do programa"""
    sistema = SistemaCadastro()
    
    print("Bem-vindo ao Sistema de Cadastro!")
    
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            # Cadastrar pessoa
            print("\n--- CADASTRAR NOVA PESSOA ---")
            nome = input("Digite o nome: ")
            
            # Validação de idade
            while True:
                try:
                    idade = int(input("Digite a idade: "))
                    if idade > 0:
                        break
                    else:
                        print("Idade deve ser maior que zero!")
                except ValueError:
                    print("Por favor, digite um número válido!")
            
            email = input("Digite o email: ")
            
            pessoa = Pessoa(nome, idade, email)
            sistema.cadastrar(pessoa)
        
        elif opcao == "2":
            # Imprimir todas as pessoas
            sistema.imprimir()
        
        elif opcao == "3":
            # Ver total de cadastros
            total = sistema.total_cadastrados()
            print(f"\nTotal de pessoas cadastradas: {total}")
        
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        
        else:
            print("\nOpção inválida! Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
