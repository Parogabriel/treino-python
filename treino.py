#atividade

'''
numeros_de_atraso = int(input("Quantos atrasos você teve? "))
if numeros_de_atraso >= 3:
    print("você está suspenso")
elif numeros_de_atraso == 2:
    print("você está em aviso")
elif numeros_de_atraso == 1 :
    print("mais dois atrasos e você está suspenso")
else:
    print("você está liberado")
'''
#atividade

'''
numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))

if numero_um > numero_dois:
    print(f"O número {numero_um} é maior que o número {numero_dois}")
elif numero_um == numero_dois:
    print(f"O número {numero_um} é igual ao número {numero_dois}")
else:
    print(f"O número {numero_um} é menor que o número {numero_dois}")
    '''

#atividade
'''
for item in range(2,11,2):
    print(item)
nomes = ["Ana", "Maria", "João", "Pedro"]
for nome in nomes:
    print(nome)
for letra in "Python":
    print(letra)
nomes = ["Ana", "Maria", "João", "Pedro"]
idades = [10, 15, 25, 30, 22, 28]
for indice in range(len(nomes)):
    print(f"{nomes[indice]} tem {idades[indice]} anos.")
    if idades[indice] >= 18:
        print("é maior de idade")
    else:
        print("é menor de idade")
senhas = ["123", "abcde", "abcd1234", "senha12345"]
for senha in senhas:
    print(f"Sua senha é: {senha}")
    if len(senha) < 6:
        print("senha fraca")
    elif len(senha) >= 6 and len(senha) <= 10:
        print("senha média")
    else:
        print("senha forte")
'''


# while exemplo 1= quando quero que criar tentativas
'''
tentativas = 0
while tentativas < 3:
    print ("tente novamente")
    tentativas += 1
    '''
# while exemplo 2 = quando queremos que o programa rode até que uma condição seja satisfeita
'''
senha = ''
while senha != 'senha123':
    senha = input("Digite a senha: ")
print("Senha correta, você está logado!")
'''
#garantir que algo esteja preenchido
'''
nome = ''
while nome == '':
    nome = input("Digite seu nome: ")
print(f"Bem vindo {nome}, ao nosso site!")
'''
#exemplo 3 = contadores
'''
horario = 0
while horario < 25:
    print(f"Agora são {horario} horas")
    horario += 1
print("Um novo dia começou!")
'''
#criar um gerenciador de login simples, no máximo 3 tentativas
#se errar 3 vezes, bloqueia o usuário
'''
usuario = ''
senha = ''
tentativas = 0
while usuario != 'admin' or senha != 'senha123':
    if tentativas == 3:
        print("Usuário bloqueado, tente novamente mais tarde.")
        break
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    tentativas += 1
else:
    print("Login realizado com sucesso!")
    '''
#listas= encontrar valores, adicionar, remover, ordenar
#exemplo 1 = encontrar indices automaticamente
'''
nomes = ["Brasil", "Espanha", "França", "Alemanha"]
print (nomes.index("Brasil"))
'''
#exemplo 2 = add novos itens
'''
salarios = [1500, 2000, 2500, 3000]
salarios_usuario= float(input("Digite o valor do seu salário: "))
salarios.append(salarios_usuario)
print(salarios)
'''
#exemplo 3 = calcule total pago aos funcionários
'''
salarios = [1500, 2000, 2500, 3000]
total = 0
for salario in salarios:
    total += salario  
print(f"O total pago aos funcionários é de R$ {total}")
'''

#fatorial
'''
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for iten in range(fatorial, numero + 1):
    fatorial *= iten
print(f"O fatorial de {numero} é {fatorial}")
'''
#chute o numero
'''
import random
numero_secreto = random.randint(1, 10)
acertou = False
while not acertou:
    chute = int(input("Digite um número entre 1 e 10: "))
    if chute > numero_secreto:
        print("Chute um número menor")
    elif chute < numero_secreto:
        print("Chute um número maior")      
    else:
        print("Parabéns, você acertou!")
        acertou = True
 '''
#velocidade maxima
'''
velocidade = float(input("Digite a velocidade do carro: "))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print("Você está dentro do limite de velocidade")
elif velocidade > velocidade_maxima + 10:
    print("Você está multado em R$ 100,00")
else:
    print("Você está multado em R$ 200,00")
 '''   

#Escreva um algoritmo que leia o nome, a idade, o salário e o sexo de uma pessoa. Imprimir a idade se for um homem e o salário se for uma mulher.
'''
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário: "))
sexo = input("Digite o sexo (M/F): ")
if sexo.upper() == "M":
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
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com {altura}m de altura é {peso_ideal:.2f} kg.")
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com {altura}m de altura é {peso_ideal:.2f} kg.")
'''    
#Escreva um algoritmo que leia o NOME, NÚMERO DE HORAS TRABALHADAS e CLASSE FUNCIONAL de um empregado da SNOB Confecções. Calcular e imprimir o salário líquido, sabendo que:
'''
Classe Funcional Salário/Hora  15,00  29,00  
Salário Bruto = Horas Trabalhadas * Salário por Hora
O salário líquido é igual ao salário bruto menos 11% de INSS.

nome = input("Digite seu nome:")
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
classe_funcional = int(input("Digite a classe funcional (1 ou 2): "))
if classe_funcional == 1:
    salario_hora = 15.00
elif classe_funcional == 2:
    salario_hora = 29.00
else:
    print("Classe funcional inválida. Por favor, insira 1 ou 2.")
    while True:
        try:
            classe_funcional = int(input("Classe funcional inválida. Digite 1 ou 2: "))
        except ValueError:
            print("Entrada inválida. Digite 1 ou 2.")
            continue
        if classe_funcional == 1:
            salario_hora = 15.00
            break
        elif classe_funcional == 2:
            salario_hora = 29.00
            break
        else:
            print("Classe funcional inválida. Por favor, insira 1 ou 2.")

salario_bruto = horas_trabalhadas * salario_hora
inss = salario_bruto * 0.11
salario_liquido = salario_bruto - inss
print(f"Funcionário: {nome}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
'''
#Escreva um algoritmo que leia o NOME e o SALÁRIO BRUTO de um funcionário. O programa deverá calcular e imprimir o salário líquido, sendo que:
'''
Salário Bruto Desconto  Até R$ 800,00 9% do salário bruto  De R$ 800,01 a R$ 1500,00 10% do salário bruto  Acima de R$ 1500,00 11% do salário bruto  
SALÁRIO LÍQUIDO = SALÁRIO BRUTO – DESCONTO

nome = input("Digite seu nome: ")
salario_bruto = float(input("Digite o salário bruto: R$ "))
if salario_bruto <= 800.00:
    desconto = salario_bruto * 0.09
elif salario_bruto <= 1500.00:
    desconto = salario_bruto * 0.10
else:
    desconto = salario_bruto * 0.11
salario_liquido = salario_bruto - desconto
print(f"O salário líquido de {nome} é R$ {salario_liquido:.2f}")
'''
#Escreva um algoritmo que leia o nome, a idade e a renda familiar de um esportista do Clube Horse. Imprimir a categoria do esportista, com base na seguinte tabela:
'''
Idade Categoria  Até 15 anos Infantil  De 16 a 18 anos Juvenil  Acima de 18 anos Adulto  
Imprimir também a classe social do esportista, com base na tabela abaixo:

Renda Familiar Classe Social  Até R$ 1.000,00 Média baixa  De R$ 1.000,01 a R$ 3.500,00 Média  Acima de R$ 3.500,00 Média alta  

nome = input("Digite o seu nome:")
idade = int(input("Digite a sua idade: "))
renda_familiar = float(input("Digite a sua renda familiar: R$ "))
if idade <= 15:
    categoria = "Infantil"
elif idade <= 18:
    categoria = "Juvenil"
else:
    categoria = "Adulto"
    if renda_familiar <= 1000.00:
        classe_social = "Média baixa"
    elif renda_familiar <= 3500.00:
        classe_social = "Média"
    else:
        classe_social = "Média alta"
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Renda Familiar: R$ {renda_familiar:.2f}")
print(f"Categoria: {categoria}")
print(f"Classe Social: {classe_social}")
'''
#Escreva um algoritmo que leia o NOME e o TURNO de uma funcionária da MARIA DA PENHA CONFECÇÕES. Imprimir o nome e o salário da funcionária, sabendo que:
'''

Turno Salário  1 R$ 450,00  2 R$ 490,00  3 R$ 650,00  
Escreva um algoritmo que leia o NOME, o CÓDIGO DO CARGO, o NÚMERO DE HORAS TRABALHADAS e o TURNO de um funcionário da PADARIA DA JUCRÉCIA. Calcular e imprimir o salário bruto, sabendo que:

Código do Cargo Salário / Hora  15,00  28,00  
Salário base = horas trabalhadas * salário por hora.

Há uma comissão por turno:

Turno Comissão  1 3% do salário base  2 4% do salário base  3 5% do salário base  

nome = input("Digite o seu nome: ")
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
codigo_cargo = int(input("Digite o código do cargo (1 ou 2): "))
turno = int(input('Digite o seu turno" (1 - Matutino, 2 - Vespertino, 3 - Noturno): '))
if codigo_cargo == 1:
    salario_base = horas_trabalhadas * 15.00
elif codigo_cargo == 2:
    salario_base = horas_trabalhadas * 28.00
else:
    print("Código de cargo inválido. Por favor, insira 1 ou 2.")
    while True:
        try:
            codigo_cargo = int(input('Código de cargo inválido. Digite 1 ou 2: '))
        except ValueError:
            print("Entrada inválida. Digite 1 ou 2.")
            continue
        if codigo_cargo == 1:
            salario_base = horas_trabalhadas * 15.00
            break
        elif codigo_cargo == 2:
            salario_base = horas_trabalhadas * 28.00
            break
        else:
            print("Código de cargo inválido. Por favor, insira 1 ou 2.")
print(f"O salário de {nome} é R$ {salario_base:.2f}")
'''



# Escreva um algoritmo que leia o NOME do responsável e o NÚMERO DE FILHOS matriculados em uma escolinha de futebol, com mensalidade de R$ 120,00. Imprimir o valor que o responsável vai pagar, baseando-se na seguinte tabela de descontos:
'''
Filhos Matriculados Desconto  1 10%  2 a 3 15%  Acima de 3 20%  

nome_responsavel = input("Digite o nome do responsável: ")
numero_filhos = int(input("Digite o número de filhos matriculados: "))
mensalidade = 120.00

if numero_filhos == 1:
    desconto = 0.10
elif 2 <= numero_filhos <= 3:
    desconto = 0.15
else:
    desconto = 0.20

valor_a_pagar = mensalidade * numero_filhos * (1 - desconto)
print(f"O valor a ser pago por {nome_responsavel} é R$ {valor_a_pagar:.2f}")
'''
#Escreva um algoritmo que leia o número do telefone, nome, número de impulsos registrados, valor total de interurbanos e tipo de telefone (1 = residencial, 2 = comercial) de um cliente da TELEMAR. Calcular e imprimir:
'''
Valor da tarifa básica.
Telefone residencial: R$ 38,14
Telefone comercial: R$ 64,69

Valor do serviço local
0,15 por impulso excedente, acima de 100 impulsos.

Tarifa de interurbanos
Valor total de interurbanos acrescidos de 5% para a Embratel.

Valor da conta
Soma de todos os serviços.

nome = input("Digite seu nome: ")
numero_telefone = input("Digite o número do telefone: ")
numero_impulsos = float(input("Digite o número de impulsos registrados: "))
valor_interurbanos = float(input("Digite o valor total de interurbanos: "))
tipo_telefone = int(input("Digite o tipo de telefone (1 - Residencial, 2 - Comercial): "))
if tipo_telefone == 1:
    tarifa_basica = 38.14
elif tipo_telefone == 2:
    tarifa_basica = 64.69   
else:
    print("Tipo de telefone inválido.")
valor_interurbanos += valor_interurbanos * 0.15
if numero_impulsos > 100:
    valor_servico_local = (numero_impulsos - 100) * 0.15
else:
    valor_servico_local = 0
valor_conta = tarifa_basica + valor_servico_local + valor_interurbanos
print(f"Cliente: {nome}")
print(f"Número do Telefone: {numero_telefone}")
print(f"Valor da Tarifa Básica: R$ {tarifa_basica:.2f}")
print(f"Valor do Serviço Local: R$ {valor_servico_local:.2f}")
print(f"Valor da Tarifa de Interurbanos: R$ {valor_interurbanos:.2f}")
print(f"Valor Total da Conta: R$ {valor_conta:.2f}")
'''