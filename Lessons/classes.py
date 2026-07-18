import random

class hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def ataque(self):
        match self.tipo:
            case "mago":
                tipo_ataque = 'magia'
            case "guerreiro":
                tipo_ataque = 'Espadada'
            case "monge":
                tipo_ataque = 'cajadada'
            case "ninja":
                tipo_ataque = 'mil anos de morte'
            case _:
                tipo_ataque = "ataque básico"

        mensagem = f"o {self.tipo} atacou usando {tipo_ataque}"
        print(mensagem)

        return mensagem


nomes_disponiveis = ["Gandalf", "Aragorn", "Lee Sin", "Naruto", "Legolas", "Saitama"]
classes_disponiveis = ["mago", "guerreiro", "monge", "ninja"]

for rodada in range(0, 4):
    print(f"\n[Rodada {rodada}]")
    
    # O Python escolhe os dados de forma aleatória aqui:
    nome_sorteado = random.choice(nomes_disponiveis)
    tipo_sorteado = random.choice(classes_disponiveis)
    idade_sorteada = random.randint(15, 150)  # Sorteia uma idade entre 15 e 150 anos
    
    # Criamos o herói com os dados que o Python acabou de sortear
    heroi_aleatorio = hero(nome_sorteado, idade_sorteada, tipo_sorteado)

    print(f"Surgiu o herói {heroi_aleatorio.nome} (Idade: {heroi_aleatorio.idade})!")
    heroi_aleatorio.ataque()



