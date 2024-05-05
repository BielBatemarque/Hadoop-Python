import sys

palavra_atual = None
contador_atual = 0

for linha in sys.stdin:
    palavra, contador = linha.strip().split("\t")

    contador = int(contador)

    if palavra_atual == palavra:
        contador_atual += contador
    else:

        if palavra_atual:
            print(f"{palavra_atual}\t{contador_atual}")

        palavra_atual = palavra
        contador_atual = contador

if palavra_atual:
    print(f"{palavra_atual}\t{contador_atual}")