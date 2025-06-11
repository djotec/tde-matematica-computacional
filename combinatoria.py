def fatorial(n):
    """Calcula o fatorial de um número inteiro n (n!)."""
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def permutacao_simples(n):
    """Retorna o número de permutações simples de n elementos (n!)."""
    return fatorial(n)

def permutacao_repeticao(n, repeticoes):
    """
    Calcula permutação com repetição:
    Fórmula: n! / (r1! * r2! * ... * rk!)
    - n: número total de elementos
    - repeticoes: lista contendo quantas vezes cada elemento se repete
    """
    if n < 0:
        raise ValueError("n deve ser não negativo.")
    if not isinstance(repeticoes, list) or any(r < 0 for r in repeticoes):
        raise ValueError("Repetições devem ser uma lista de inteiros não negativos.")
    
    denominador = 1
    for r in repeticoes:
        denominador *= fatorial(r)
    return fatorial(n) // denominador

def combinacao(n, k):
    """
    Calcula combinação simples (n escolhe k):
    Fórmula: n! / (k! * (n-k)!)
    """
    if k < 0 or k > n:
        raise ValueError("k deve estar entre 0 e n.")
    return fatorial(n) // (fatorial(k) * fatorial(n - k))
