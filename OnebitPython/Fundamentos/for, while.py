frutas = ["maça", "banana", "uva"]

for fruta in frutas:
    print(fruta)

for index, fruta in enumerate(frutas):
    print(index, fruta)

"""for numero in range(0, 1001, 5):
    print(numero)
    if numero == 100:
        break"""

contador = 1

while contador <= 10:
    print(contador)
    contador += 1