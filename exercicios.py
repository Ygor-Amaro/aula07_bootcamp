# 1 - Calcular Média de Valores em uma Lista

# teste = [1, 2, 3, 4, 5]

# def media(lista: list) -> float:
#     """
#     Calcula a média de uma lista de números.
#     Parâmetros:
#         lista (list): Lista de números.
#     Retorna:
#         float: Média dos números na lista.
#     """
#     if not lista:
#         return 0
#     return sum(lista) / len(lista)

# media(teste)
# print(f"Média: {media(teste)}")

# 2 - Filtrar Dados Acima de um Limite

teste = [1, 2, 3, 4, 5]

def filtro(lista: list[float], limite: float) -> list[float]:
    """
    Filtra os valores de uma lista que estão acima de um limite.
    Parâmetros:
        lista (list): Lista de números.
        limite (float): Limite para filtrar os números.
    Retorna:
        list: Lista com os números acima do limite.
    """
    return [x for x in lista if x > limite]

print(filtro(teste, 3.5))

# 3 - Contar Valores Únicos em uma Lista


# 4 - Converter Celsius para Fahrenheit em uma Lista


# 5 - Calcular Desvio Padrão de uma Lista


# 6 - Encontrar Valores Ausentes em uma Sequência

