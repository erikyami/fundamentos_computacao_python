#EXE04 da lista 01

A = float(input("Informe o lado A: "))
B = float(input("Informe o lado B: "))
C = float(input("Informe o lado C: "))

# Verifica forma um triangulo:
if ((A > B + C) or (B > A + C) or (C > A + B)):
    print("Os valores formados não formam um triângulo")
# Verifica se é um triangulo equilátero    
elif ((A == B) and (B == C)):
    print("Os valores formam um triângulo equilátero")
# Verifica se é um triangulo escaleno    
elif ((A != B) and (B != C) and (A != C)):
    print("Os valores formam um triângulo escaleno")
else:
    #Resta ser um trinâgulo isosceles
    print("Os valores formam um triângulo isósceles")