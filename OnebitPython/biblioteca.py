class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        novo_livro = {"titulo": titulo, "autor": autor}
        self.livros.append(novo_livro)

        return f"Registrado o livro {titulo}, de {autor} na {self.nome}"

    def buscar_livro(self, termo_busca):
        print(f"Acervo da {self.nome}")
        busca = termo_busca.lower()

        texto_resultados = f"--- Resultados para '{termo_busca}' ---\n"
        encontrou_algum = False

        for livro in self.livros:
            titulo_limpo = livro['titulo'].lower()
            autor_limpo = livro['autor'].lower()

            if busca in titulo_limpo or busca in autor_limpo:
                texto_resultados += f"\n {livro['titulo']} (Autor: {livro['autor']})"
                encontrou_algum = True

        if encontrou_algum == True:
            return texto_resultados
        else:
            return f"O livro não foi encontrado nas estantes da {self.nome}"

    def listar_acervo(self):
        texto = (f"Acervo da {self.nome}:")
        for livro in self.livros:
            texto += f"\n- {livro['titulo']} de {livro['autor']} -"

        return texto


bib = Biblioteca("Biblioteca Municipal")
print(bib.adicionar_livro("O PROCESSO", "FRANZ KAFKA"))
print(bib.adicionar_livro("A METAMORFOSE", "FRANZ KAFKA"))
print(bib.adicionar_livro("Harry Potter e a Pedra Filosofa", "J.K. ROWLING"))
print(bib.listar_acervo())

print(bib.buscar_livro('kafka'))




