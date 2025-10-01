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
#for item in range(2,11,2):
#    print(item)
#nomes = ["Ana", "Maria", "João", "Pedro"]
#for nome in nomes:
 #   print(nome)
#for letra in "Python":
 #   print(letra)
#nomes = ["Ana", "Maria", "João", "Pedro"]
#idades = [10, 15, 25, 30, 22, 28]
#for indice in range(len(nomes)):
 #   print(f"{nomes[indice]} tem {idades[indice]} anos.")
  #  if idades[indice] >= 18:
   #     print("é maior de idade")
    #else:
     #   print("é menor de idade")
#senhas = ["123", "abcde", "abcd1234", "senha12345"]
#for senha in senhas:
 #   print(f"Sua senha é: {senha}")
  #  if len(senha) < 6:
   #     print("senha fraca")
    #elif len(senha) >= 6 and len(senha) <= 10:
     #   print("senha média")
   # else:
    #    print("senha forte")



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