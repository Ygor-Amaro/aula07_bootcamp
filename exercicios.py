# 1 - Calcular Média de Valores em uma Lista

teste = [1, 2, 3, 4, 5]

def media(lista: list) -> float:
    """
    Calcula a média de uma lista de números.
    Parâmetros:
        lista (list): Lista de números.
    Retorna:
        float: Média dos números na lista.
    """
    if not lista:
        return 0
    return sum(lista) / len(lista)

media(teste)
print(f"Média: {media(teste)}")

# 2 - Filtrar Dados Acima de um Limite


# 3 - Contar Valores Únicos em uma Lista


# 4 - Converter Celsius para Fahrenheit em uma Lista


# 5 - Calcular Desvio Padrão de uma Lista


# 6 - Encontrar Valores Ausentes em uma Sequência

