"""Desafio: Análise de Vendas de Produtos Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, 
 o desafio consiste em ler os dados, processá-los em um dicionário para análise e, por fim, calcular e reportar as vendas totais por categoria de produto.
 """

#Tarefas:
#   Ler o arquivo CSV e carregar os dados.
#   Processar os dados em um dicionário, onde a chave é a categoria, e o valor é uma lista de dicionários, cada um contendo informações do produto (Produto, Quantidade, Venda).
#   Calcular o total de vendas (Quantidade * Venda) por categoria.
    # Funções
    #   Ler CSV:
    #       Função: ler_csv
    #       Entrada: Nome do arquivo CSV
    #       Saída: Lista de dicionários com dados lidos
    #   Processar Dados:
    #       Função: processar_dados
    #       Entrada: Lista de dicionários
    #       Saída: Dicionário processado conforme descrito
    #   Calcular Vendas por Categoria:
    #       Função: calcular_vendas_categoria
    #       Entrada: Dicionário processado
    #       Saída: Dicionário com total de vendas por categoria


def ler_csv(arquivo):
    """
    Lê um arquivo CSV e retorna uma lista de dicionários com os dados lidos.
    
    Parâmetros:
    arquivo (str): Nome do arquivo CSV a ser lido.
    
    Retorna:
    list: Lista de dicionários com os dados lidos do CSV.
    """
    import csv
    with open(arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

