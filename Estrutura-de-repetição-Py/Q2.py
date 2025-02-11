# Um supermercado está fazendo o balanço do estoque. Para isso,
# pediu sua ajuda para construir um programa que solicite a
# quantidade de produtos existentes no estoque. Para cada produto,
# solicite o nome e a quantidade. O programa deve informar a
# situação do produto no estoque:
# - Sem estoque: se a quantidade for zero.
# - Estoque baixo: se a quantidade for maior que zero e
# menor que 10.
# - Estoque suficiente: se a quantidade for maior ou igual a 10.

# Solicitar a quantidade de produtos no estoque
qtde_produtos = int(input("Quantos produtos existem no estoque? "))

# Loop para solicitar o nome e a quantidade de cada produto
for i in range(qtde_produtos):
    nome_produto = input("Qual o nome do produto? ")
    quantidade_produto = int(input("Qual a quantidade de produtos? "))

    # Verificar a situação do estoque
    if quantidade_produto == 0:
        print(f"{nome_produto}: Sem estoque")
    elif 0 < quantidade_produto < 10:
        print(f"{nome_produto}: Estoque baixo")
    else:
        print(f"{nome_produto}: Estoque suficiente")

