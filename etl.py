import csv 
from collections import defaultdict
path_arquivo = "produtos.csv"

#Função que ler um arquivo CSV e retorna uma lista de dicionários.
def ler_csv(nome_do_arquivo_csv: str) -> list[dict]: 
    codificacoes = ['utf-8', 'ISO-8859-1', 'cp1252']
    lista = []
    with open(nome_do_arquivo_csv, mode="r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

# Função para calcular o total de vendas por categoria

def calcular_vendas_categoria(lista: list[dict]) -> dict:
    vendas_por_categoria = defaultdict(float)  # Inicializa com 0.0 por padrão
    for item in lista:
        categoria = item['Categoria']
        quantidade = int(item['Quantidade'])
        preco = float(item['Preco'].replace(',', '.'))
        total_venda = quantidade * preco
        vendas_por_categoria[categoria] += total_venda
    return dict(vendas_por_categoria)  # Converte defaultdict para dict

# Leitura dos dados do CSV
vendas_itens = ler_csv(path_arquivo)

# Cálculo do total de vendas por categoria
vendas_totais = calcular_vendas_categoria(vendas_itens)

print("\nSoma dos Valores por Categoria:")
for categoria, total in vendas_totais.items():
    print(f"{categoria}: {total:.2f}")


