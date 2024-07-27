import csv 
path_arquivo = "vendas.csv"

#Função que ler um arquivo CSV e retorna uma lista de dicionários.
def ler_csv(nome_do_arquivo_csv: str) -> list[dict]: 
    codificacoes = ['utf-8', 'ISO-8859-1', 'cp1252']
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

vendas_itens: list[dict]
vendas_itens = ler_csv(path_arquivo)
print(vendas_itens)

# Função para calcular o total de vendas por categoria
#def calcular_vendas_categoria


