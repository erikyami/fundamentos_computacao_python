#EXE03 da lista 01

salario_por_hora = float(input("Informe o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))

salario_bruto = salario_por_hora * horas_trabalhadas

desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

total_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print("+Salário Bruto: R$",salario_bruto)
print("-IR (11%): R$", desconto_ir)
print("-INSS (8%): R$", desconto_inss)
print("-Sindicato (5%): R$", desconto_sindicato)
print("=Salário Líquido: R$", salario_liquido)