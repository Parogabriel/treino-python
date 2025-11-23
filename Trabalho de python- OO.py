import re

class Carro:
    def __init__(self):
        self.fabricante = ""
        self.tipo = ""
        self.modelo = ""
        self.ano = 0       
        self.cor = ""
        self.placa = ""

    def cadastrar(self):
        print("\n" + "="*15 + " NOVO VEÍCULO " + "="*15)

        dados_veiculos = {
            "VOLKSWAGEN": {
                "HATCH": ["GOL", "POLO", "UP"],
                "SEDAN": ["VIRTUS", "VOYAGE", "JETTA"],
                "SUV": ["T-CROSS", "NIVUS", "TAOS"],
                "PICKUP": ["AMAROK", "SAVEIRO"]
            },
            "CHEVROLET": {
                "HATCH": ["ONIX"],
                "SEDAN": ["ONIX PLUS", "CRUZE"],
                "SUV": ["TRACKER", "TRAILBLAZER", "EQUINOX"],
                "PICKUP": ["S10", "MONTANA"]
            },
            "FIAT": {
                "HATCH": ["ARGO", "MOBI"],
                "SEDAN": ["CRONOS"],
                "SUV": ["PULSE", "FASTBACK"],
                "PICKUP": ["TORO", "STRADA"]
            },
            "TOYOTA": {
                "HATCH": ["YARIS"],
                "SEDAN": ["COROLLA", "YARIS SEDAN", "CAMRY"],
                "SUV": ["COROLLA CROSS", "SW4", "RAV4"],
                "PICKUP": ["HILUX"]
            },
            "HONDA": {
                "HATCH": ["CITY HATCH"],
                "SEDAN": ["CITY", "CIVIC", "ACCORD"],
                "SUV": ["HR-V", "ZR-V", "CR-V"]
            },
            "JEEP": {
                "SUV": ["RENEGADE", "COMPASS", "COMMANDER", "WRANGLER"]
            },
            "FORD": {
                "PICKUP": ["RANGER", "MAVERICK", "F-150"],
                "SUV": ["BRONCO", "TERRITORY"],
                "ESPORTIVO": ["MUSTANG"]
            },
            "BMW": {
                "SEDAN": ["SERIE 3", "SERIE 5"],
                "SUV": ["X1", "X3", "X5", "X6"]
            },
            "HYUNDAI": {
                "HATCH": ["HB20"],
                "SEDAN": ["HB20S"],
                "SUV": ["CRETA", "TUCSON"]
            }
        }
#fabricante
        while True:
            print(f"Marcas: {', '.join(dados_veiculos.keys())}")
            marca_input = input("Digite o fabricante: ").upper().strip()
            
            if marca_input in dados_veiculos:
                self.fabricante = marca_input
                break
            else:
                print("Marca não registada. Tente novamente.\n")

#tipo
        opcoes_tipos = dados_veiculos[self.fabricante]
        
        while True:
            print(f"\nCategorias da {self.fabricante}: {', '.join(opcoes_tipos.keys())}")
            tipo_input = input("Digite a categoria: ").upper().strip()
            
            if tipo_input in opcoes_tipos:
                self.tipo = tipo_input
                lista_modelos_finais = opcoes_tipos[tipo_input]
                break
            else:
                print(f"A {self.fabricante} não possui a categoria '{tipo_input}'.")

#modelo
        while True:
            print(f"\nModelos disponíveis ({self.tipo}): {', '.join(lista_modelos_finais)}")
            modelo_input = input("Digite o modelo: ").upper().strip()
            
            if modelo_input in lista_modelos_finais:
                self.modelo = modelo_input
                break
            else:
                print("Modelo inválido. Escolha um da lista acima.")
#ano
        ano_valido = range(1960, 2027)
        while True:
            try:
                ano_input = int(input("Digite o ano de fabricação (1960-2026): "))
                if ano_input in ano_valido:
                    self.ano = ano_input
                    break
                else:
                    print("Ano inválido! Deve estar entre 1960 e 2026.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número válido para o ano.")
#cor   
        cor_valida = ["BRANCO", "PRETO", "PRATA", "CINZA", "VERMELHO", "AZUL", "VERDE", "AMARELO", "BEGE", "LARANJA"]
        while True:
            cor = input("Digite a cor do veículo:").upper()
            if cor in cor_valida:
                self.cor = cor.title()
                break
            else:
                print("Cor inválida! Tente novamente.")

#placa
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
        print(f"Tipo:       {self.tipo}")
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

# Primeiramente, no desenvolvimento inical do código, desenvolvi uma estrtura simples de cadastro. 
# Porém, vi que o sistema de placas não funcionava bem sem uma estrutura correta. 
# Após desenvolver uma solução, percebi que poderia melhorar toda a estrtura para tornar mais específico os veículos cadastrados. 
# 3Assim crie a base, porém eles não se relacionavam. Então, com os conhecimentos da aula de bancos de dadosm, criei uma base hierárquica para relacionar os dados e tornar o cadastro mais fluído e específico.
