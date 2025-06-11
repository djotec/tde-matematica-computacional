from estatistica import soma, media

def testar_soma():
    dados = [2, 4, 6, 8]
    esperado = 20
    resultado = soma(dados)
    print("Teste soma:")
    print(f"Entrada: {dados}")
    print(f"Resultado esperado: {esperado}")
    print(f"Resultado obtido:   {resultado}")
    print("Passou\n" if resultado == esperado else " Falhou\n")

def testar_media():
    dados = [5, 10, 15]
    esperado = 10
    resultado = media(dados)
    print("Teste média:")
    print(f"Entrada: {dados}")
    print(f"Resultado esperado: {esperado}")
    print(f"Resultado obtido:   {resultado}")
    print("Passou\n" if resultado == esperado else " Falhou\n")

# Rodar os testes
if __name__ == "__main__":
    testar_soma()
    testar_media()
