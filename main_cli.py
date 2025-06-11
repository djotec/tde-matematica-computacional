# main.py

from combinatoria import fatorial, permutacao_simples, permutacao_repeticao, combinacao
from casas_de_pombo import principio_casas_pombo
from estatistica import soma, media, variancia, desvio_padrao
from probabilidade import intersecao, probabilidade_condicional
from recorrencia import fatorial_rec, coeficiente_binomial, fibonacci_rec


def menu_combinatoria():
    print("\n=== Combinatória ===")
    print("1 - Fatorial")
    print("2 - Permutação simples")
    print("3 - Permutação com repetição")
    print("4 - Combinação")
    opc = input("Escolha a opção: ")
    try:
        if opc == "1":
            n = int(input("Digite um número inteiro não negativo: "))
            print(f"Fatorial de {n} é {fatorial(n)}")
        elif opc == "2":
            n = int(input("Digite um número inteiro não negativo: "))
            print(f"Permutação simples de {n} é {permutacao_simples(n)}")
        elif opc == "3":
            n = int(input("Digite o número total de elementos (n): "))
            reps_str = input("Digite as repetições separadas por vírgula (ex: 2,3,1): ")
            repeticoes = [int(x.strip()) for x in reps_str.split(",")]
            print(f"Permutação com repetição é {permutacao_repeticao(n, repeticoes)}")
        elif opc == "4":
            n = int(input("Digite o valor de n (total de elementos): "))
            k = int(input("Digite o valor de k (elementos escolhidos): "))
            print(f"Combinação C({n},{k}) é {combinacao(n, k)}")
        else:
            print("Opção inválida.")
    except Exception as e:
        print(f"Erro: {e}")


def menu_casas_pombo():
    print("\n=== Princípio das Casas de Pombo ===")
    try:
        itens = int(input("Digite o número de itens: "))
        grupos = int(input("Digite o número de grupos: "))
        print(principio_casas_pombo(itens, grupos))
    except Exception as e:
        print(f"Erro: {e}")


def menu_estatistica():
    print("\n=== Estatística ===")
    print("Digite os números separados por vírgula (ex: 10,20,30):")
    try:
        dados_str = input()
        dados = [float(x.strip()) for x in dados_str.split(",") if x.strip()]
        print(f"Soma: {soma(dados)}")
        print(f"Média: {media(dados)}")
        print(f"Variância: {variancia(dados)}")
        print(f"Desvio Padrão: {desvio_padrao(dados)}")
    except Exception as e:
        print(f"Erro: {e}")


def menu_probabilidade():
    print("\n=== Probabilidade ===")
    try:
        print("Digite os elementos do evento A separados por vírgula:")
        a_str = input()
        evento_a = [x.strip() for x in a_str.split(",") if x.strip()]

        print("Digite os elementos do evento B separados por vírgula:")
        b_str = input()
        evento_b = [x.strip() for x in b_str.split(",") if x.strip()]

        print("Digite todos os elementos do espaço amostral separados por vírgula:")
        espaco_str = input()
        espaco = [x.strip() for x in espaco_str.split(",") if x.strip()]

        inter = intersecao(evento_a, evento_b)
        print(f"Interseção entre A e B: {inter} elementos")
        p_cond = probabilidade_condicional(evento_a, evento_b, espaco)
        print(f"Probabilidade condicional P(A|B): {p_cond:.4f}")
    except Exception as e:
        print(f"Erro: {e}")


def menu_recorrencia():
    print("\n=== Recorrência ===")
    print("1 - Fatorial recursivo")
    print("2 - Coeficiente binomial (combinação) recursivo")
    print("3 - Fibonacci recursivo")
    opc = input("Escolha a opção: ")
    try:
        if opc == "1":
            n = int(input("Digite um número inteiro não negativo: "))
            print(f"Fatorial recursivo de {n} é {fatorial_rec(n)}")
        elif opc == "2":
            n = int(input("Digite o valor de n: "))
            k = int(input("Digite o valor de k: "))
            print(f"Coeficiente binomial C({n},{k}) é {coeficiente_binomial(n, k)}")
        elif opc == "3":
            n = int(input("Digite o índice n da sequência de Fibonacci: "))
            print(f"Fibonacci({n}) = {fibonacci_rec(n)}")
        else:
            print("Opção inválida.")
    except Exception as e:
        print(f"Erro: {e}")


def main():
    while True:
        print("\n=== Menu Principal ===")
        print("1 - Combinatória")
        print("2 - Princípio das Casas de Pombo")
        print("3 - Estatística")
        print("4 - Probabilidade")
        print("5 - Recorrência")
        print("0 - Sair")
        opc = input("Escolha a opção: ")

        if opc == "1":
            menu_combinatoria()
        elif opc == "2":
            menu_casas_pombo()
        elif opc == "3":
            menu_estatistica()
        elif opc == "4":
            menu_probabilidade()
        elif opc == "5":
            menu_recorrencia()
        elif opc == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
