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
#atividade


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


#Escreva um algoritmo que leia o nome, a idade, o salário e o sexo de uma pessoa. Imprimir a idade se for um homem e o salário se for uma mulher.

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário: "))
sexo = input("Digite o sexo (M/F): ")
if sexo.upper() == "M":
    print(f"A idade de {nome} é {idade}.")
elif sexo.upper() == "F":
    print(f"O salário de {nome} é {salario}.")

#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7 * h) – 58
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

#Escreva um algoritmo que leia o NOME, NÚMERO DE HORAS TRABALHADAS e CLASSE FUNCIONAL de um empregado da SNOB Confecções. Calcular e imprimir o salário líquido, sabendo que:

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

#Escreva um algoritmo que leia o NOME e o SALÁRIO BRUTO de um funcionário. O programa deverá calcular e imprimir o salário líquido, sendo que:

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




# Escreva um algoritmo que leia o NOME do responsável e o NÚMERO DE FILHOS matriculados em uma escolinha de futebol, com mensalidade de R$ 120,00. Imprimir o valor que o responsável vai pagar, baseando-se na seguinte tabela de descontos:

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

#Escreva um algoritmo que leia o número do telefone, nome, número de impulsos registrados, valor total de interurbanos e tipo de telefone (1 = residencial, 2 = comercial) de um cliente da TELEMAR. Calcular e imprimir:

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
    valor_servico_local = (numero_impulsos - 100) * 0,05
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
#Escreva um algoritmo que leia o NOME, NÚMERO DE HORAS TRABALHADAS e SALÁRIO POR HORA de 10 funcionários da NEW EMPIRE CONFECÇÕES. Calcular e imprimir o salário líquido de cada um, sendo que:

'''
SALÁRIO BRUTO = HORAS TRABALHADAS * SALÁRIO POR HORA
INSS = 11% DO SALÁRIO BRUTO
SALÁRIO LÍQUIDO = SALÁRIO BRUTO - INSS
'''
'''
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
#Uma certa firma fez uma pesquisa de mercado para saber se as pessoas gostaram ou não de um certo produto lançado. Para isso, preencheu uma ficha com o SEXO do entrevistado e sua RESPOSTA (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, faça um algoritmo que calcule e imprima:
#pessoas que responderam sim.
#pessoas que responderam não.
# a porcentagem de pessoas do sexo feminino que responderam sim em relação ao total de pessoas do sexo feminino entrevistadas.
'''
total_sim = 0
total_nao = 0   
total_feminino = 0
total_feminino_sim = 0
for i in range(2000):
    sexo = input("Digite o sexo do entrevistado (M/F): ")
    resposta = input("Você gostou do produto? (sim/não): ")
    if resposta == 'sim':
        total_sim += 1
        if sexo == 'F':
            total_feminino_sim += 1
    elif resposta == 'não':
        total_nao += 1
    if sexo == 'F':
        total_feminino += 1
if total_feminino > 0:
    porcentagem_feminino_sim = (total_feminino_sim / total_feminino) * 100
    print(f"Porcentagem de mulheres que responderam sim: {porcentagem_feminino_sim:.2f}%")
else:
    print("Não há mulheres cadastradas.")
print(f"Total de pessoas que responderam sim: {total_sim}")
print(f"Total de pessoas que responderam não: {total_nao}")
print(f"Total de mulheres entrevistadas: {total_feminino}")
'''
#O programador responsável pelo sistema do CEFET resolveu fazer um programa para processar as fichas com os dados dos alunos. Cada ficha contém o NOME, SEXO, IDADE, TURNO (1 para manhã, 2 para tarde e 3 para noite) e SÉRIE do aluno (1 para primeiro ano, 2 para segundo e 3 para terceiro). Construa um algoritmo que leia os dados dos alunos e calcule e imprima:
#O numro de alunos matriculados no turno da noite.
# O numero de alunos que estão na terceira série.
#O numero de mulheres na segunda série.
'''
total_noite = 0
total_terceira_serie = 0
total_mulheres_segunda_serie = 0
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome  == 'sair':
        break
    sexo = input("Digite o sexo do aluno (M/F): ")
    idade = int(input("Digite a idade do aluno: "))
    turno = int(input("Digite o turno do aluno (1 - Manhã, 2 - Tarde, 3 - Noite): "))
    serie = int(input("Digite a série do aluno (1 - Primeiro ano, 2 - Segundo ano, 3 - Terceiro ano): "))
    if turno == 3:
        total_noite += 1
    if serie == 3:
        total_terceira_serie += 1
    if sexo == 'F' and serie == 2:
        total_mulheres_segunda_serie += 1
print(f"Total de alunos matriculados no turno da noite: {total_noite}")
print(f"Total de alunos na terceira série: {total_terceira_serie}")
print(f"Total de mulheres na segunda série: {total_mulheres_segunda_serie}")
'''
# Fazer contagem regressiva de 10 a 1

'''
time = 10000000
while time >= 1:
    print(time)
    time -= 1
print("foguete lançado!")
'''
#47. A MARIA DA PENHA CONFECÇÕES mantém um cadastro de seus funcionários com os seguintes dados:
'''
total_folha_pagamento = 0
maior_salario = 0   
nome_maior_salario = ''
idade_mulher_mais_velha = 0
nome_mulher_mais_velha = ''
for i in range(350):
    nome = input("Digite o nome do funcionário: ")
    classe_funcional = int(input("Digite a classe funcional (1, 2, 3 ou 4): "))
    idade = int(input("Digite a idade do funcionário: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
    sexo = input("Digite o sexo do funcionário (M/F): ").upper()
    if classe_funcional == 1:
        salario_hora = 10.00
    elif classe_funcional == 2:
        salario_hora = 15.00
    elif classe_funcional == 3:
        salario_hora = 18.00
    elif classe_funcional == 4:
        salario_hora = 25.00
    else:
        print("Classe funcional inválida.")
        continue
    salario = horas_trabalhadas * salario_hora
    total_folha_pagamento += salario
    print(f"O salário de {nome} é R$ {salario:.2f}")
    if salario > maior_salario:
        maior_salario = salario
        nome_maior_salario = nome
    if sexo == 'F' and idade > idade_mulher_mais_velha:
        idade_mulher_mais_velha = idade
        nome_mulher_mais_velha = nome
print(f"O maior salário é R$ {maior_salario:.2f}, recebido por {nome_maior_salario}.")
if nome_mulher_mais_velha:
    print(f"A mulher mais velha é {nome_mulher_mais_velha}, com {idade_mulher_mais_velha} anos.")
print(f"O total da folha de pagamento é R$ {total_folha_pagamento:.2f}")
'''
#48
'''
total_feminino = 0
total_masculino = 0
soma_idade_homens_experiencia = 0
total_homens_experiencia = 0
total_homens_menos_35_experiencia = 0
total_mulheres_mais_35_experiencia = 0
menor_idade_mulheres_experiencia = float('inf')
inscricoes_mulheres_mais_35_experiencia = []
for i in range(3823):
    numero_inscricao = input("Digite o número de inscrição do candidato: ")
    idade = int(input("Digite a idade do candidato: "))
    sexo = input("Digite o sexo do candidato (M/F): ").upper()
    experiencia = input("O candidato tem experiência no serviço? (SIM/NÃO): ").upper()
    if sexo == 'F':
        total_feminino += 1
        if experiencia == 'SIM' and idade > 35:
            total_mulheres_mais_35_experiencia += 1
            inscricoes_mulheres_mais_35_experiencia.append(numero_inscricao)
            if idade < menor_idade_mulheres_experiencia:
                menor_idade_mulheres_experiencia = idade
    elif sexo == 'M':
        total_masculino += 1
        if experiencia == 'SIM':
            soma_idade_homens_experiencia += idade
            total_homens_experiencia += 1
            if idade < 35:
                total_homens_menos_35_experiencia += 1
print(f"Total de candidatos do sexo feminino: {total_feminino}")
print(f"Total de candidatos do sexo masculino: {total_masculino}")
if total_homens_experiencia > 0:
    media_idade_homens_experiencia = soma_idade_homens_experiencia / total_homens_experiencia
    print(f"Média de idade dos homens com experiência no serviço: {media_idade_homens_experiencia:.2f} anos")
else:
    print("Não há homens com experiência no serviço.")
porcentagem_homens_menos_35_experiencia = (total_homens_menos_35_experiencia / total_masculino) * 100 if total_masculino > 0 else 0
print(f"Porcentagem de homens com menos de 35 anos e experiência no serviço: {porcentagem_homens_menos_35_experiencia:.2f}%")
print(f"Total de mulheres com mais de 35 anos e experiência no serviço: {total_mulheres_mais_35_experiencia}")
if menor_idade_mulheres_experiencia != float('inf'):
    print(f"A menor idade entre as mulheres com experiência no serviço: {menor_idade_mulheres_experiencia} anos")
    print(f"Números de inscrição das mulheres com experiência no serviço: {inscricoes_mulheres_mais_35_experiencia}")
    print(f"Total de mulheres com mais de 35 anos e experiência no serviço: {total_mulheres_mais_35_experiencia}")
'''
#49
grau_de_instrução = int(input("Digite o grau de instrução (1, 2, 3 ou 4): "))
total_candidatos = 0
total_masculino = 0
total_feminino = 0
total_mulheres_segundo_grau = 0
total_homens_terceiro_grau = 0
while True:
    grau_de_instrucao = int(input("Digite o grau de instrução (1 - Segundo grau, 2 - Terceiro grau) ou 0 para encerrar: "))
    if grau_de_instrucao == 0:
        break
    nome = input("Digite o nome do candidato: ")
    sexo = input("Digite o sexo do candidato (M/F): ").upper()
    total_candidatos += 1
    if sexo == 'M':
        total_masculino += 1
        if grau_de_instrucao == 2:
            total_homens_terceiro_grau += 1
    elif sexo == 'F':
        total_feminino += 1
        if grau_de_instrucao == 1:
            total_mulheres_segundo_grau += 1
print(f"Total de candidatos: {total_candidatos}")
print(f"Total de candidatos do sexo masculino: {total_masculino}")
print(f"Total de candidatos do sexo feminino: {total_feminino}")
print(f"Total de mulheres com apenas o segundo grau: {total_mulheres_segundo_grau}")
if total_masculino > 0:
    porcentagem_homens_terceiro_grau = (total_homens_terceiro_grau / total_masculino) * 100
    print(f"Porcentagem de homens com terceiro grau: {porcentagem_homens_terceiro_grau:.2f}%")
else:
    print("Não há homens inscritos.")