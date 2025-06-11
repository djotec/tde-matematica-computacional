
# Função recursiva para fatorial com memoização
def fatorial_rec(n, memo=None):
    """
    Calcula o fatorial de n usando recursão com memoização.
    fatorial(0) = 1
    """
    if n < 0:
        raise ValueError("n deve ser inteiro não negativo.")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 1
    else:
        memo[n] = n * fatorial_rec(n - 1, memo)
    return memo[n]


# Função recursiva para coeficiente binomial (combinação) com memoização
def coeficiente_binomial(n, k, memo=None):
    """
    Calcula o coeficiente binomial C(n, k) usando relação de recorrência:
    C(n, k) = C(n-1, k-1) + C(n-1, k)
    com C(n, 0) = C(n, n) = 1
    """
    if memo is None:
        memo = {}
    if (n, k) in memo:
        return memo[(n, k)]
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        memo[(n, k)] = 1
    else:
        memo[(n, k)] = coeficiente_binomial(n - 1, k - 1, memo) + coeficiente_binomial(n - 1, k, memo)
    return memo[(n, k)]


# Sequência de Fibonacci com memoização
def fibonacci_rec(n, memo=None):
    """
    Calcula o n-ésimo termo da sequência de Fibonacci usando recursão e memoização.
    fibonacci(0) = 0, fibonacci(1) = 1
    """
    if n < 0:
        raise ValueError("n deve ser inteiro não negativo.")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_rec(n - 1, memo) + fibonacci_rec(n - 2, memo)
    return memo[n]

