while True:
    n = int(input("Informe um valor inteiro menor que 1000 [0 para sair]: "))
    if n == 0:
        break
    if n >= 1000:
        print("Valor inválido!")
    else:
        ## // pega a parte inteira da divisao 
        centenas = n // 100
        # % pega o resto da divisao
        n = n % 100
        
        dezenas = n // 10
        unidades = n % 10
        
        texto_cem = 'centena'
        texto_dez = 'dezena'
        texto_un = 'unidade'
        
        if centenas > 1:
            texto_cem = 'centenas'
        if dezenas > 1:
            texto_dez = 'dezenas'
        if unidades > 1:
            texto_un = 'unidades'    

        texto_final = ""   
        if centenas > 0:
            texto_final = str(centenas) +" "+texto_cem
            
        if dezenas > 0:
            if unidades > 0:
                if centenas > 0:
                    texto_final = texto_final+", "
                texto_final = texto_final+str(dezenas)+" "+texto_dez+" e "+str(unidades)+" "+texto_un
            else:
                if centenas > 0:
                    texto_final = texto_final+" e "
                texto_final = texto_final+str(dezenas)+" "+texto_dez
        elif unidades > 0:
            if centenas > 0:
                texto_final = texto_final+" e "
            texto_final = texto_final + str(unidades)+" "+texto_un
        print(texto_final)
    