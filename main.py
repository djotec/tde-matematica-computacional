from combinatoria import permutacao_simples, permutacao_repeticao, combinacao
from casas_de_pombo import principio_casas_pombo
from probabilidade import probabilidade_condicional
from recorrencia import fibonacci
from estatistica import media, variancia, desvio_padrao

def menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Permutação Simples")
    print("2. Permutação com Repetição")
    print("3. Combinação")
    print("4. Princípio das Casas de Pombo")
    print("5. Probabilidade Condicional")
    print("6. Fibonacci (Relação de Recorrência)")
    print("7. Estatística Básica")
    print("0. Sair")

def executar():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            n = int(input("Digite o valor de n: "))
            print("Resultado:", permutacao_simples(n))

        elif opcao == "2":
            n = int(input("Digite o valor de n: "))
            repeticoes = input("Digite as repetições separadas por vírgula (ex: 2,2,3): ")
            repeticoes = [int(x.strip()) for x in repeticoes.split(",")]
            print("Resultado:", permutacao_repeticao(n, repeticoes))

        elif opcao == "3":
            n = int(input("Digite o valor de n: "))
            k = int(input("Digite o valor de k: "))
            print("Resultado:", combinacao(n, k))

        elif opcao == "4":
            itens = int(input("Digite o número de itens: "))
            recipientes = int(input("Digite o número de recipientes: "))
            print("Resultado:", principio_casas_pombo(itens, recipientes))

        elif opcao == "5":
            intersecao = float(input("Digite P(A ∩ B): "))
            p_b = float(input("Digite P(B): "))
            print("Resultado:", probabilidade_condicional(intersecao, p_b))

        elif opcao == "6":
            n = int(input("Digite o valor de n para Fibonacci(n): "))
            print("Resultado:", fibonacci(n))

        elif opcao == "7":
            dados = input("Digite os dados separados por vírgula: ")
            lista = [float(x.strip()) for x in dados.split(",")]
            print("Média:", media(lista))
            print("Variância:", variancia(lista))
            print("Desvio Padrão:", desvio_padrao(lista))

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()
