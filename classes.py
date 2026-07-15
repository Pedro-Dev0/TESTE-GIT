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

    
meu_heroi = hero('pedro', 23, 'ninja')
meu_heroi.ataque()




