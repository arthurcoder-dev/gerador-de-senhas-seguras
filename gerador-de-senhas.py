import secrets

print("="*10," GERADOR DE SENHAS SEGURAS ","="*10)

# Criação das variáveis
possiveis = ""
senha = ""
tamanho_da_senha = int(input("\nBem-vindo(a) ao Gerador de Senha Seguras\n\nPor favor, insira o número de caracteres que a senha deve ter:\n"))

# Criação dos caractéres
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "111222333444555666777888999"
simbolos = "!@#$%&*"

# Confirmações
add_maiusculas = input("Deseja letras maiúsculas? (s/n):\n").lower()
add_minusculas = input("Deseja letras minúsculas? (s/n):\n").lower()
add_numeros = input("Deseja números? (s/n):\n").lower()
add_simbolos = input("Deseja símbolos? (s/n):\n").lower()

# Detecta os caracteres escolhidos e guarda eles na variável
if add_maiusculas == "s":
    possiveis = possiveis + maiusculas
if add_minusculas == "s":
    possiveis = possiveis + minusculas
if add_numeros == "s":      
    possiveis = possiveis + numeros
if add_simbolos == "s":
    possiveis = possiveis + simbolos

# Detecta se a quantidade de caracteres na senha é menor que o escolhido e, se sim
while len(senha) < tamanho_da_senha:
    escolhas = secrets.choice(possiveis)
    senha = senha + escolhas

# Resultado
if senha:
    print(f"Senha Gerada: {senha}")
else:
    print("Você precisa escolher pelo menos 1 tipo caractere")