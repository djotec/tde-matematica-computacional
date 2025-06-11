def intersecao(evento_a, evento_b):
    """
    Retorna o número de elementos em comum entre os dois eventos.
    """
    return len(set(evento_a).intersection(set(evento_b)))


def probabilidade_condicional(evento_a, evento_b, espaco_amostral):
    """
    Calcula a probabilidade condicional P(A|B) = P(A ∩ B) / P(B)
    Onde:
        - evento_a: lista com os elementos do evento A
        - evento_b: lista com os elementos do evento B
        - espaco_amostral: lista com todos os possíveis resultados
    """
    total = len(espaco_amostral)
    if total == 0:
        raise ValueError("Espaço amostral não pode ser vazio.")

    inter = intersecao(evento_a, evento_b)
    prob_intersecao = inter / total
    prob_b = len(evento_b) / total

    if prob_b == 0:
        raise ValueError("Probabilidade de B é zero. P(A|B) indefinido.")

    return prob_intersecao / prob_b
