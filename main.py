import tkinter as tk
from tkinter import ttk
from combinatoria import fatorial, permutacao_simples, permutacao_repeticao, combinacao
from casas_de_pombo import principio_casas_pombo
from estatistica import soma, media, variancia, desvio_padrao
from probabilidade import intersecao, probabilidade_condicional
from recorrencia import fatorial_rec, coeficiente_binomial, fibonacci_rec


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Matemática")
        self.geometry("600x400")
        self.resizable(False, False)

        self.menu_frame = ttk.Frame(self)
        self.menu_frame.pack(pady=10)

        self.content_frame = ttk.Frame(self)
        self.content_frame.pack(pady=10)

        # Menu reorganizado
        botoes = [
            ("Combinatória", self.menu_combinatoria),
            ("Casas de Pombo", self.menu_casas_pombo),
            ("Probabilidade", self.menu_probabilidade),
            ("Recorrência", self.menu_recorrencia),
            ("Estatística", self.menu_estatistica),
        ]
        for i, (txt, cmd) in enumerate(botoes):
            ttk.Button(self.menu_frame, text=txt, command=cmd).grid(row=0, column=i, padx=5)

        self.menu_combinatoria()  # Exibe por padrão

    def limpar_conteudo(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def criar_input(self, labels, btn_text, calcular_callback):
        self.limpar_conteudo()
        entradas = []

        for i, texto in enumerate(labels):
            ttk.Label(self.content_frame, text=texto).grid(row=i, column=0, sticky="w", pady=2)
            e = ttk.Entry(self.content_frame, width=40)
            e.grid(row=i, column=1, pady=2)
            entradas.append(e)

        resultado_label = ttk.Label(self.content_frame, text="", justify="left")
        resultado_label.grid(row=len(labels)+1, column=0, columnspan=2, pady=10)

        def on_calcular():
            try:
                vals = [e.get() for e in entradas]
                res = calcular_callback(vals)
                resultado_label.config(text=res)
            except Exception as ex:
                resultado_label.config(text=f"Erro: {ex}")

        ttk.Button(self.content_frame, text=btn_text, command=on_calcular).grid(row=len(labels), column=0, columnspan=2, pady=5)

    # --- Menus ---

    def menu_combinatoria(self):
        self.limpar_conteudo()
        ttk.Label(self.content_frame, text="Escolha uma operação combinatória:").grid(row=0, column=0, pady=5)

        ops = [
            ("Fatorial", self.calc_fatorial),
            ("Permutação simples", self.calc_permutacao_simples),
            ("Permutação com repetição", self.calc_permutacao_repeticao),
            ("Combinação", self.calc_combinacao),
        ]
        for i, (txt, cmd) in enumerate(ops):
            ttk.Button(self.content_frame, text=txt, command=cmd).grid(row=i+1, column=0, sticky="ew", pady=2)

    def calc_fatorial(self):
        def cb(vals):
            n = int(vals[0])
            return f"Fatorial de {n} é {fatorial(n)}"
        self.criar_input(["Número inteiro não negativo:"], "Calcular", cb)

    def calc_permutacao_simples(self):
        def cb(vals):
            n = int(vals[0])
            return f"Permutação simples de {n} é {permutacao_simples(n)}"
        self.criar_input(["Número inteiro não negativo:"], "Calcular", cb)

    def calc_permutacao_repeticao(self):
        def cb(vals):
            n = int(vals[0])
            repeticoes = [int(x.strip()) for x in vals[1].split(",") if x.strip()]
            return f"Permutação com repetição é {permutacao_repeticao(n, repeticoes)}"
        self.criar_input(["Total de elementos (n):", "Repetições (ex: 2,3,1):"], "Calcular", cb)

    def calc_combinacao(self):
        def cb(vals):
            n, k = map(int, vals)
            return f"Combinação C({n},{k}) é {combinacao(n,k)}"
        self.criar_input(["n (total elementos):", "k (escolhidos):"], "Calcular", cb)

    def menu_casas_pombo(self):
        def cb(vals):
            itens, grupos = map(int, vals)
            return f"Resultado: {principio_casas_pombo(itens, grupos)}"
        self.criar_input(["Número de itens:", "Número de grupos:"], "Calcular", cb)

    def menu_probabilidade(self):
        def cb(vals):
            A = [x.strip() for x in vals[0].split(",") if x.strip()]
            B = [x.strip() for x in vals[1].split(",") if x.strip()]
            S = [x.strip() for x in vals[2].split(",") if x.strip()]
            inter = intersecao(A, B)
            p_cond = probabilidade_condicional(A, B, S)
            return f"Interseção A ∩ B: {inter}\nProbabilidade condicional P(A|B): {p_cond:.4f}"
        self.criar_input(
            ["Elementos evento A (ex: a,b,c):",
             "Elementos evento B (ex: a,b,c):",
             "Espaço amostral (ex: a,b,c,d):"],
            "Calcular", cb)

    def menu_recorrencia(self):
        self.limpar_conteudo()
        ttk.Label(self.content_frame, text="Escolha uma operação recursiva:").grid(row=0, column=0, pady=5)

        ops = [
            ("Fatorial recursivo", self.calc_fatorial_rec),
            ("Coeficiente binomial", self.calc_coef_binomial),
            ("Fibonacci recursivo", self.calc_fibonacci_rec),
        ]
        for i, (txt, cmd) in enumerate(ops):
            ttk.Button(self.content_frame, text=txt, command=cmd).grid(row=i+1, column=0, sticky="ew", pady=2)

    def calc_fatorial_rec(self):
        def cb(vals):
            n = int(vals[0])
            return f"Fatorial recursivo de {n} é {fatorial_rec(n)}"
        self.criar_input(["Número inteiro não negativo:"], "Calcular", cb)

    def calc_coef_binomial(self):
        def cb(vals):
            n, k = map(int, vals)
            return f"Coeficiente binomial C({n},{k}) é {coeficiente_binomial(n,k)}"
        self.criar_input(["n:", "k:"], "Calcular", cb)

    def calc_fibonacci_rec(self):
        def cb(vals):
            n = int(vals[0])
            return f"{n}º número de Fibonacci (recursivo) é {fibonacci_rec(n)}"
        self.criar_input(["Posição n:"], "Calcular", cb)

    def menu_estatistica(self):
        def cb(vals):
            dados = [float(x.strip()) for x in vals[0].split(",") if x.strip()]
            return (f"Soma: {soma(dados)}\n"
                    f"Média: {media(dados)}\n"
                    f"Variância: {variancia(dados)}\n"
                    f"Desvio padrão: {desvio_padrao(dados)}")
        self.criar_input(["Números separados por vírgula:"], "Calcular", cb)


if __name__ == "__main__":
    app = App()
    app.mainloop()
