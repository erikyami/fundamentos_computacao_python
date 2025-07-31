valor1 = int(input("Informe o primeiro valor: "))
menor = maior = valor1
valor2 = int(input("Informe o segundo valor: "))
if valor2 > maior:
    maior = valor2
if valor2 < menor:
    menor = valor2    
valor3 = int(input("Informe o terceiro valor: "))
if valor3 > maior:
    maior = valor3
if valor3 < menor:
    menor = valor3

print(f"Valor maior: {maior}, Valor menor: {menor}")