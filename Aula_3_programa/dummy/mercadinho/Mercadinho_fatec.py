# author = Vinicius EZ
# version: 1.0.1
# date: abr/09/2022
# description: Este programa cadastra usuários
# name: Mercadinho fatec

from hashlib import sha256
import sys
from time import sleep
import os

print(os.getcwd())



# Mensagem de boas vindas
mensagem = "Olá, seja bem-vindo ao Mercadinho Fatec"

# Imprimindo mensagem de boas vindas como máquina de escrever
for letra in mensagem:
    sys.stdout.write(letra)
    sys.stdout.flush()
#    sleep(0.1)
print()
    

# Setando as opções do menu
opcoes_de_menu = ["sign in", "sign up", "fale conosco"]
    
# Imprimindo menu de opções    
count = 1
for opcao in opcoes_de_menu:
    print(f"[{count}] - {opcao}")
    count += 1
  
# prompt    
opcao_digitada = input("Qual opção deseja?")

# Abrindo arquivo csv para leitura
with open("db.csv") as arquivo:
    print(arquivo.read())
