#Programa para verificar se um usário é maior, ou menor de idade
qtd_habitantes = int(input("Qual a quantidade de habitantes, na cidade de Tianguá?"))
for i in range (qtd_habitantes):

    nome = input("Qual é o seu nome?")
    sexo = input("Qual é o seu sexo ")
    idade = int(input("Qual a sua idade? "))
    if idade >= 18:
        print("Maior de idade")
    else:
         print("Menor de idade")

