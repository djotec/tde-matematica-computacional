def soma(lista):
    total = 0
    for valor in lista:
        total += valor
    return total

def media(dados):
    if not dados:
        return 0
    return soma(dados) / len(dados)

def variancia(dados):
    if not dados:
        return 0
    m = media(dados)
    soma_diferencas_quadrado = 0
    for valor in dados:
        diferenca = valor - m
        soma_diferencas_quadrado += diferenca * diferenca
    return soma_diferencas_quadrado / len(dados)

def desvio_padrao(dados):
    v = variancia(dados)
    if v == 0:
        return 0
    # Raiz quadrada com método de Newton-Babilônico
    x = v
    for _ in range(10):
        x = 0.5 * (x + v / x)
    return x
