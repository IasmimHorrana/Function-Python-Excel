from etl import ler_csv, calcular_vendas_categoria

path_arquivo = "produtos.csv"

vendas_itens = ler_csv(path_arquivo)
vendas_totais = calcular_vendas_categoria(vendas_itens)
print("\nSoma dos Valores por Categoria:")
for categoria, total in vendas_totais.items():
    print(f"{categoria}: {total:.2f}")
