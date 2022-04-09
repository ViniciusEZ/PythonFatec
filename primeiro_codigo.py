# import random

# Código digitado pelo usuário
# entrada_do_usuario = 7
# numero_que_deve_ser_advinhado = 7
# 
# if entrada_do_usuario == numero_que_deve_ser_advinhado:
#     print("Você acertou!😞")
# else:    
#     print("Você errou!!!😀")


# Programa com número aleatório

import random
numero_que_deve_ser_advinhado = random.randint(1, 10)
entrada_do_usuario = int(input("Digite um valor aqui: "))

# numero_que_deve_ser_advinhado = random.randint(1, 10)

if entrada_do_usuario == numero_que_deve_ser_advinhado:
    print("Você acertou!😀")
else:    
    print("Você errou!!!😞")















