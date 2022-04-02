from re import A


entrada_user = input("Digite uma letra: ")

if entrada_user.lower() in "aeiou":
    print("Vogal")
else:
    print("Consoante")    