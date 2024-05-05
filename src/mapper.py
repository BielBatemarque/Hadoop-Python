import sys

for line in sys.stdin:
    palavras = line.strip().split()

    for palavra in palavras:
        print(f"{palavra}\t1")