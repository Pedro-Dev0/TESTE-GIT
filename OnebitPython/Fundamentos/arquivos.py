"""arquivo = open("ola.txt")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()"""

"""with open("ola.txt" "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)"""

with open("ola.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("ATT do conteudo\n")