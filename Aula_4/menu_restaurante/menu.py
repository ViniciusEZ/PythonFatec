# lendo o banco de dados
def ler_banco():
    """Essas função lê um banco de dados"""
    with open("estoque.csv", "r") as file:
        dados_do_banco = file.read() #pegando os dados em formato de texto
        dados_do_estoque = dados_do_banco.split("\n") # quebrando em linhas
        menu = dados_do_estoque[0].split(",")
        quantidades_no_estoque = dados_do_estoque[1].split(",")
        
        return menu, quantidades_no_estoque
    
itens_do_menu = ler_banco()[0]
estoque_do_menu = ler_banco()[1]

print("Faça seu pedido: ")
for posicao, item in enumerate(itens_do_menu):
    print(f"[{posicao + 1}] - {item}")
pedido = int(input(">>> "))

tamanho_menu = len(itens_do_menu) # len sempre retorna números inteiros
if pedido > tamanho_menu or pedido < 1:
    print("Opção inválida")

# tirando a máscara do input + 1
pedido -= 1
estoque_do_menu[pedido] = str(int(estoque_do_menu[pedido]) - 1)
#print(estoque_do_menu)

with open("estoque.csv", "w") as file:
    file.write(",".join(itens_do_menu))
    file.write("\n")
    file.write(",".join(estoque_do_menu))
    
    
    
          
    

    

    