# Importar a bilioteca pandas e usar o alias "pd"
import pandas as pd

# Usar a função 'read_csv' do pandas e atribuir o retorno para a variável 'df' | DataFrame
df = pd.read_csv("./0TA_PRECO_MEDICAMENTO.csv",encoding='ISO-8859-1', sep=';', low_memory=False)

# Criar uma função para exibir o menu
def exibir_menu():
    print("1 - para as 5 primeiras linhas")
    print("2 - para as 5 últimas linhas")
    print("3 - Medicamentos com restrição")
    print("4 - Não Comercializados em 2020")
    print("5 - Comercializados em 2020")
    print("6 - para sair")


## Inicia um Loop Inifinito
while True:
    # Chama a função 'exibir_menu()'
    exibir_menu()
    opcao = int(input("Insira uma opção: "))
    
    if opcao == 1:
        #Imprime as 5 primeiras Linhas com a função 'head'
        print(df.head(5))
    elif opcao == 2:
        #Imprime as 5 últimas Linhas com a função 'tail'
        print(df.tail(5))
    elif opcao == 3:
        # Filtra os resultados onde a coluna 'RESTRIÇÃO HOSPITALAR' == "Sim" e armazena na variável 'df_restricao'
        df_restricao = df[df['RESTRIÇÃO HOSPITALAR'] == "Sim"]
        # Mostra na Tela o resultado
        print(df_restricao)
    elif opcao == 4:
        # Filtra os resultados onde a coluna 'COMERCIALIZAÇÃO 2020' == "Não" e armazena na variável 'df_2020'
        df_2020 = df[df['COMERCIALIZAÇÃO 2020'] == "Não"]
        # Mostra na Tela o resultado
        print(df_2020)
    elif opcao == 5:
        # Filtra os resultados onde a coluna 'COMERCIALIZAÇÃO 2020' == "Sim" e armazena na variável 'df_2020'
        df_2020 = df[df['COMERCIALIZAÇÃO 2020'] == "Sim"]
        # Mostra na Tela o resultado
        print(df_2020)
    elif opcao == 6:
        # Encerra o Loop Infinito se a opção == 6
        break       