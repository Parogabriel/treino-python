#Cadastro de veículos
#Criar um programa OO em Python para cadastrar, ao menos, cinco veículos.
#O programa deve possuir ao menos dois métodos: cadastrar e imprimir.
#A classe “carro” deve possuir, ao menos, cinco atributos: cor, ano, modelo, fabricante e placa
import re
class Carro:
    def __init__(self):
        self.fabricante = ""
        self.modelo = ""
        self.ano = 0
        self.cor = ""
        self.placa = ""

    def cadastrar(self):
        print("\n--- Novo Cadastro ---")
        self.fabricante = input("Digite o fabricante: ")
        self.modelo = input("Digite o modelo: ")

        while True:
            try:
                self.ano = int(input("Digite o ano:"))
                break
            except ValueError:
                print("Por favor, digite um número válido para o ano.")
        
        self.cor = input("Digite a cor: ")
        while True:
            placa_input = input("Digite a placa (ex: ABC1234): ").upper()
            if re.match(r'^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$', placa_input):
                self.placa = placa_input
                break
            else:
                print("Formato de placa inválido! Tente novamente.")
        print("Carro cadastrado com sucesso!")

    def imprimir(self):
        print("-" * 30)
        print(f"Fabricante: {self.fabricante}")
        print(f"Modelo:     {self.modelo}")
        print(f"Ano:        {self.ano}")
        print(f"Cor:        {self.cor}")
        print(f"Placa:      {self.placa}")
        print("-" * 30)

if __name__ == "__main__":
    lista_de_carros = [] 
    print("Bem-vindo ao Sistema de Cadastro de Veículos")
    for i in range(5):
        print(f"\nCadastrando o veículo {i + 1} de 5:")        
        novo_carro = Carro()
        novo_carro.cadastrar()   
        lista_de_carros.append(novo_carro)

    print("\n" + "="*10 + " RELATÓRIO DE FROTA " + "="*10)
    for veiculo in lista_de_carros:
        veiculo.imprimir()