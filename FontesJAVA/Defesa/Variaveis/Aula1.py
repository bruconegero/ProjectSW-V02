nome = input("Digite o nome: ")
nac = float(input("Digite a NAC: "))
am = float(input("Digite a AM: "))
ps = float(input("Digite a PS: "))
faltas = int(input("digite as faltas: "))
media = nac * 0.2 + am * 0.3 + ps * 0.5
print (type(nome))
print (type(nac))
print ("A Média do", nome, "é:", media)
if faltas >20:
    print("Reprovado por falta")
else:
    if media >=6:
        print("Aprovado")
    elif media <4:
        print("DP")
    else:
        print("Exame")
print("até logo...")
