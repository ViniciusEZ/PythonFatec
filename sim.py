tamanho_minimo = 6
compras = ["arroz", "picanha", "azeitona", "chocolate", "feijão", "batata", "sushi", "papel higiênico", "pasta de dente", "vinho", "salgadinho", "carne moida", "leite"]
for item in compras:
    if len(item) < tamanho_minimo:
        pass
    
    else:
        print(item)
        