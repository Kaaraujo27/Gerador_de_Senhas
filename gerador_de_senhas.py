import random
import string

quantidade = int(input("Quantos caracteres sua senha terá? "))
especiais = int(input("Quantos caracteres especiais ela terá? "))

caracteres = string.ascii_letters + string.digits + string.punctuation

letras = string.ascii_letters 
numeros = string.digits 
simbolos = string.punctuation

senha = ""

quantidade_normal = quantidade - especiais
caracteres_normais = letras + numeros

for i in range(quantidade):
    senha += random.choice(caracteres)

for i in range(especiais):
    senha += random.choice(simbolos)

for i in range(quantidade_normal):
    senha += random.choice(caracteres_normais)

lista_senha = list(senha) 
random.shuffle(lista_senha)

print("Senha gerada:", senha)