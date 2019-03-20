nome = input("Digite o nome: ")
idade = int(input("digite a idade: "))
if idade <16:
    print("não vota")
elif idade <=17 or idade >65:
    print("facultativo")
else:
    print("Obrigatório")

