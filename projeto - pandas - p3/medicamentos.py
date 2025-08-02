# Importar a bilioteca pandas e usar o alias "pd"
import pandas as pd

# Usar a função 'read_csv' do pandas e atribuir o retorno para a variável 'df' | DataFrame
df = pd.read_csv("./0TA_PRECO_MEDICAMENTO.csv",encoding='ISO-8859-1', sep=';', low_memory=False)

# Função para exibir o menu na tela
def exibir_menu():
    print("1 - para as 5 primeiras linhas")
    print("2 - para as 5 últimas linhas")
    print("3 - Medicamentos com restrição")
    print("4 - Não Comercializados em 2020")
    print("5 - Comercializados em 2020")
    print("6 - Buscar produto por regime de preço")
    print("7 - para sair")

# Função para renomear colunas do dataframe
def renomear_colunas(dataframe):
    # Dicionário para renomear colunas
    # De: Para
    novos_nomes_coluna = {
        'SUBSTÂNCIA': 'substancia',
        'CNPJ': 'cnpj',
        'LABORATÓRIO': 'laboratorio',
        'CÓDIGO GGREM': 'cod_ggrem',
        'REGISTRO': 'registro',
        'EAN 1': 'ean_1',
        'EAN 2': 'ean_2',
        'EAN 3': 'ean_3',
        'PRODUTO': 'produto',
        'APRESENTAÇÃO': 'apresentacao',
        'CLASSE TERAPÊUTICA': 'classe_terapeutica',
        'TIPO DE PRODUTO (STATUS DO PRODUTO)': 'status_produto',
        'REGIME DE PREÇO': 'regime_de_preco',
        'PF Sem Impostos': 'pf_sem_imposto',
        'PF 0%': 'pf_0_porcento',
        'PF 12%': 'pf_12_porcento',
        'PF 17%': 'pf_17_porcento',
        'PF 17% ALC': 'pf_17_alc_porcento',
        'PF 17,5%': 'pf_17_5_porcento',
        'PF 17,5% ALC': 'pf_17_5_alc_porcento',
        'PF 18%': 'pf_18_porcento',
        'PF 18% ALC': 'pf_18_alc_porcento',
        'PF 20%': 'pf_20_porcento',
        'PMC 0%': 'pmc_0_porcento',
        'PMC 12%': 'pmc_12_porcento',
        'PMC 17%': 'pmc_17_porcento',
        'PMC 17% ALC': 'pmc_17_alc_porcento',
        'PMC 17,5%': 'pmc_17_5_porcento',
        'PMC 17,5% ALC': 'pmc_17_5_alc_porcento',
        'PMC 18%': 'pmc_18_porcento',
        'PMC 18% ALC': 'pmc_18_alc_porcento',
        'PMC 20%': 'pmc_20_porcento',
        'RESTRIÇÃO HOSPITALAR': 'restricao_hospitalar',
        'CAP': 'cap',
        'CONFAZ 87': 'confaz_87',
        'ICMS 0%': 'icms_0_porcento',
        'ANÁLISE RECURSAL': 'analise_recursal',
        'LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)': 'lista_credito_tributario',
        'COMERCIALIZAÇÃO 2020': 'comercializado_2020',
        'TARJA': 'tarja'
    }

    # Renomear colunas
    dataframe.rename(columns=novos_nomes_coluna, inplace=True)


# Função para preencher valores vazios
# fillna - preenche valores vazios ou nulos
def preencher_valores_vazios(dataframe):
    for coluna in dataframe.columns:
        dataframe[coluna].fillna('Não Informado')
        print(f"Valores ausentes na coluna '{coluna}' preenchidos com 'Não Informado'.")

# Função para buscar produtos por regime de preço
def busca_produto_por_regime_de_preco(dataframe):
    regime = input("Digite o regime de preço [ Liberado | Regulado ]: ")
    if regime == "Liberado" or regime == "Regulado":
        resultado = dataframe[dataframe['regime_de_preco'].str.contains(regime)]
        print(f"\n--- Produtos com o regime '{regime}' ---")
        print(resultado[['produto', 'substancia', 'laboratorio', 'pf_sem_imposto']])
    else:
        print("você digitou um regime inválido")


# Tratamento de dados
# Chama a função renomear_colunas
renomear_colunas(df)

# Chama a função para preencher valores vazios
preencher_valores_vazios(df)

## Inicia um Loop Inifinito
while True:
    # Chama a função 'exibir_menu()'
    exibir_menu()
    
    #Solicita ao usuário que escolha uma opção de 1 a 7
    opcao = int(input("Insira uma opção: "))
    
    if opcao == 1:
        #Imprime as 5 primeiras Linhas com a função 'head'
        print(df.head(5))
    elif opcao == 2:
        #Imprime as 5 últimas Linhas com a função 'tail'
        print(df.tail(5))
    elif opcao == 3:
        # Filtra os resultados onde a coluna 'restricao_hospitalar' == "Sim"
        resultado = df[df['restricao_hospitalar'] == "Sim"]
        # Mostra na Tela o resultado
        print(resultado)
    elif opcao == 4:
        # Filtra os resultados onde a coluna 'comercializado_2020' == "Não"
        resultado = df[df['comercializado_2020'] == "Não"]
        # Mostra na Tela o resultado
        print(resultado)
    elif opcao == 5:
        # Filtra os resultados onde a coluna 'comercializado_2020' == "Sim"
        resultado = df[df['comercializado_2020'] == "Sim"]
        # Mostra na Tela o resultado
        print(resultado)
        # Buscar produto por regime de preço [ Liberado | Regulado ]
    elif opcao == 6:
        busca_produto_por_regime_de_preco(df)
    elif opcao == 7:
        # Encerra o Loop Infinito se a opção == 6
        print("Saindo do Aplicativo")
        break
    else:
        # Caso não seja uma opção de 1 a 6
        print("Opção Inválida - Tente Novamente")     