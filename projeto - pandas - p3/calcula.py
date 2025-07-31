def total(jucara, agua, esp, qtde):
    total_agua = agua * 10
    total_jucara = jucara * 3
    total_esp = esp
    soma_total = total_agua + total_jucara + total_esp
    total_geral = soma_total * qtde
    return total_geral

print(total(3,4,5,5))