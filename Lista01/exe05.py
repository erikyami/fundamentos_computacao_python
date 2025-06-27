#EXE05 da lista 01

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))

media = (n1+n2+n3)/3

if (media >= 9.1 and media <= 10):
    conceito = "A"
elif (media >= 7.6 and media <= 9):
    conceito = "B"
elif (media >= 6.1 and media <= 7.5):
    conceito = "C"
elif (media >= 4.1 and media <=6):
    conceito = "D"
elif (media >= 0 and media <= 4):
    conceito = "E"
else:
    conceito = "Valores inválidos"


if media >= 6.1 and media <= 10:
    print("APROVADO, conceito:", conceito)
    print("Média: ",media)
elif (media > 0 and media <= 6):
    print("REPROVADO, conceito:", conceito)
    print("Média: ",media)
else:
    print("Notas inválidas")