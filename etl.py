import csv 
path_arquivo = "vendas.csv"

#Função que ler um arquivo CSV e retorna uma lista de dicionários.
def ler_csv(nome_do_arquivo_csv: str) -> list[dict]: 
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

#vendas_itens: list[dict]
#vendas_itens = ler_csv(path_arquivo)
#print(vendas_itens)

# Função para calcular o total de vendas por categoria
def calcular_vendas_categoria(lista: list[dict[str, str]]) -> dict[str, float]:
    vendas_por_categoria = {}
    for produto in lista:
        categoria = produto['Categoria']
        quantidade = int(produto['Quantidade'])
        venda = float(produto['Venda'].replace(',', '.'))
        total_venda = quantidade * venda
        if categoria in vendas_por_categoria:
            vendas_por_categoria[categoria] += total_venda
        else:
            vendas_por_categoria[categoria] = total_venda
    return vendas_por_categoria
"""
# Exibição dos resultados
print("\nTotal de Vendas por Categoria:")
for categoria, total_vendas in vendas_totais.items():
    print(f"{categoria}: {total_vendas:.2f}")
"""