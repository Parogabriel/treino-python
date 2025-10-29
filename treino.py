#atividade

'''
numeros_de_atraso = int(input("Quantos atrasos você teve? "))
if numeros_de_atraso >= 3:
print("você está suspenso")
@@ -10,10 +9,9 @@
print("mais dois atrasos e você está suspenso")
else:
print("você está liberado")
'''
#atividade

'''

numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))

@@ -154,10 +152,10 @@
print("Você está multado em R$ 100,00")
else:
print("Você está multado em R$ 200,00")
 '''   


#Escreva um algoritmo que leia o nome, a idade, o salário e o sexo de uma pessoa. Imprimir a idade se for um homem e o salário se for uma mulher.
'''

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário: "))
@@ -166,11 +164,11 @@
print(f"A idade de {nome} é {idade}.")
elif sexo.upper() == "F":
print(f"O salário de {nome} é {salario}.")
'''

#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:
'''Para homens: (72.7 * h) – 58
Para mulheres: (62.1 * h) – 44.7 (h = altura)'''
'''

altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M/F): ")
if sexo.upper() == "M":
@@ -179,9 +177,9 @@
elif sexo.upper() == "F":
peso_ideal = (62.1 * altura) - 44.7
print(f"O peso ideal para uma mulher com {altura}m de altura é {peso_ideal:.2f} kg.")
'''    

#Escreva um algoritmo que leia o NOME, NÚMERO DE HORAS TRABALHADAS e CLASSE FUNCIONAL de um empregado da SNOB Confecções. Calcular e imprimir o salário líquido, sabendo que:
'''

Classe Funcional Salário/Hora  15,00  29,00  
Salário Bruto = Horas Trabalhadas * Salário por Hora
O salário líquido é igual ao salário bruto menos 11% de INSS.
@@ -215,9 +213,9 @@
salario_liquido = salario_bruto - inss
print(f"Funcionário: {nome}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
'''

#Escreva um algoritmo que leia o NOME e o SALÁRIO BRUTO de um funcionário. O programa deverá calcular e imprimir o salário líquido, sendo que:
'''

Salário Bruto Desconto  Até R$ 800,00 9% do salário bruto  De R$ 800,01 a R$ 1500,00 10% do salário bruto  Acima de R$ 1500,00 11% do salário bruto  
SALÁRIO LÍQUIDO = SALÁRIO BRUTO – DESCONTO

@@ -298,12 +296,12 @@
else:
print("Código de cargo inválido. Por favor, insira 1 ou 2.")
print(f"O salário de {nome} é R$ {salario_base:.2f}")
'''




# Escreva um algoritmo que leia o NOME do responsável e o NÚMERO DE FILHOS matriculados em uma escolinha de futebol, com mensalidade de R$ 120,00. Imprimir o valor que o responsável vai pagar, baseando-se na seguinte tabela de descontos:
'''

Filhos Matriculados Desconto  1 10%  2 a 3 15%  Acima de 3 20%  

nome_responsavel = input("Digite o nome do responsável: ")
@@ -319,9 +317,9 @@

valor_a_pagar = mensalidade * numero_filhos * (1 - desconto)
print(f"O valor a ser pago por {nome_responsavel} é R$ {valor_a_pagar:.2f}")
'''

#Escreva um algoritmo que leia o número do telefone, nome, número de impulsos registrados, valor total de interurbanos e tipo de telefone (1 = residencial, 2 = comercial) de um cliente da TELEMAR. Calcular e imprimir:
'''

Valor da tarifa básica.
Telefone residencial: R$ 38,14
Telefone comercial: R$ 64,69
@@ -358,148 +356,4 @@
print(f"Valor do Serviço Local: R$ {valor_servico_local:.2f}")
print(f"Valor da Tarifa de Interurbanos: R$ {valor_interurbanos:.2f}")
print(f"Valor Total da Conta: R$ {valor_conta:.2f}")
'''

#Escreva um algoritmo que leia o NOME, NÚMERO DE HORAS TRABALHADAS e SALÁRIO POR HORA de 10 funcionários da NEW EMPIRE CONFECÇÕES. Calcular e imprimir o salário líquido de cada um, sendo que:
'''

SALÁRIO BRUTO = HORAS TRABALHADAS * SALÁRIO POR HORA
INSS = 11% DO SALÁRIO BRUTO
SALÁRIO LÍQUIDO = SALÁRIO BRUTO - INSS


for i in range(10):
    nome = input("Digite o nome do funcionário: ")
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
    salario_por_hora = float(input("Digite o salário por hora: "))
    salario_bruto = horas_trabalhadas * salario_por_hora
    inss = salario_bruto * 0.11
    salario_liquido = salario_bruto - inss
    print(f"O salário líquido de {nome} é R$ {salario_liquido:.2f}")
'''
#Escreva um algoritmo que leia o NOME, a MODALIDADE ESPORTIVA (1 = Voley, 2 = Basquete, 3 = Futsal), a IDADE e o SEXO (M ou F) de 10 atletas do clube "LES ENFANTS". Calcular e imprimir:
'''
Média de idade dos homens.
Média de idade das mulheres.
Porcentagem de mulheres matriculadas no basquete, em relação ao número de mulheres matriculadas.
Número de homens com idade entre 25 e 30 anos.

total_homens = 0
total_mulheres = 0
soma_idade_homens = 0
soma_idade_mulheres = 0
mulheres_basquete = 0
for i in range(2):
    nome = input("Digite o nome do atleta: ")
    modalidade = int(input("Digite a modalidade esportiva (1 - Voley, 2 - Basquete, 3 - Futsal): "))
    idade = int(input("Digite a idade do atleta: "))
    sexo = input("Digite o sexo do atleta (M/F): ").upper()
    if sexo == 'M':
        total_homens += 1
        soma_idade_homens += idade
        if 25 <= idade <= 30:
            total_homens_25_30 += 1
    elif sexo == 'F':
        total_mulheres += 1
        soma_idade_mulheres += idade
        if modalidade == 2:
            mulheres_basquete += 1
if total_homens > 0:
    media_idade_homens = soma_idade_homens / total_homens
    print(f"Média de idade dos homens: {media_idade_homens:.2f} anos")
else:
    print("Não há homens cadastrados.")
if total_mulheres > 0:
    media_idade_mulheres = soma_idade_mulheres / total_mulheres
    porcentagem_mulheres_basquete = (mulheres_basquete / total_mulheres) * 100
    print(f"Média de idade das mulheres: {media_idade_mulheres:.2f} anos")
    print(f"Porcentagem de mulheres no basquete: {porcentagem_mulheres_basquete:.2f}%")
else:
    print("Não há mulheres cadastradas.")
    '''
#Construir um algoritmo que leia NOME e IDADE de 300 pessoas e que calcule e imprima:
'''
a) A soma de idade das pessoas.
b) Os nomes das pessoas com idade maior ou igual a 21 anos.

from tkinter.font import names
import random


soma_idades = 0
nomes_maiores_21 = []

primeiros_nomes = [
    "Ana", "Maria", "João", "Pedro", "Gabriel", "Lucas", "Mariana", "Beatriz",
    "Felipe", "Carla", "Bruno", "Rafael", "Juliana", "Camila", "Larissa",
    "Thiago", "Daniel", "Luana", "Paulo", "Sofia", "Isabela", "Matheus",
    "Gustavo", "Fernanda", "Diego", "André", "Rodrigo", "Carolina", "Renata",
    "Eduardo", "Aline"

for _ in range(300):
    nome = random.choice(primeiros_nomes)
    idade = random.randint(1, 23)
    soma_idades += idade
    if idade >= 21:
        nomes_maiores_21.append(nome)

print(f"Soma de idades: {soma_idades}")
print("Nomes das pessoas com 21 anos ou mais:")
for nome in nomes_maiores_21:
    print(nome)
    '''

#Construir um algoritmo que leia NOME, ALTURA e SEXO de um grupo indeterminado de pessoas e que calcule e imprima:
'''
a) A média de altura dos homens.
b) A maior altura.
c) A menor altura.

total_homens = 0
soma_altura_homens = 0
maior_altura = 0
menor_altura = float('inf')
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    altura = float(input("Digite a altura da pessoa em metros: "))
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()
    if sexo == 'M':
        total_homens += 1
        soma_altura_homens += altura
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
if total_homens > 0:
    media_altura_homens = soma_altura_homens / total_homens
    print(f"Média de altura dos homens: {media_altura_homens:.2f} metros")
else:
    print("Não há homens cadastrados.")
print(f"Maior altura: {maior_altura:.2f} metros")
print(f"Menor altura: {menor_altura:.2f} metros")
'''

#Elaborar um algoritmo que leia NOME, HORAS TRABALHADAS, SALÁRIO-HORA e SEXO de um grupo de operários e que calcule e imprima:
'''

a) Salário total dos funcionários.
b) O maior salário, juntamente com o Nome de quem o recebeu.

total_salarios = 0
maior_salario = 0
nome_maior_salario = ''
while True:
    nome = input("Digite o nome do operário (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
    salario_hora = float(input("Digite o salário por hora: "))
    sexo = input("Digite o sexo do operário (M/F): ").upper()
    salario = horas_trabalhadas * salario_hora
    total_salarios += salario
    if salario > maior_salario:
        maior_salario = salario
        nome_maior_salario = nome
'''