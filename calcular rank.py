def calcular_rank(vitorias, derrotas):
    
    saldo_vitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif vitorias >= 11 and vitorias <= 21:
        nivel = "Bronze"
    elif vitorias >= 21 and vitorias <= 50:
        nivel = "Prata"
    elif vitorias >= 51 and vitorias <= 80:
        nivel = "Ouro"
    elif vitorias >= 81 and vitorias <= 90:
        nivel = "Diamante"
    elif vitorias >= 91 and vitorias <= 100:
        nivel = "Lendário"
    elif vitorias >= 101:
        nivel = "Imortal"
    
    return f"O Herói tem o saldo de {saldo_vitorias} e está no {nivel}"
    

resultado = calcular_rank(101,0)
print(resultado)