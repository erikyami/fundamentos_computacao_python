valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))

lista = [valor1,valor2,valor3]
lista.sort()

for n in lista:
    print(n)
    