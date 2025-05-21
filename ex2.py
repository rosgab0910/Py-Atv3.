palavra = input("Digite uma palavra: ")

vogais = "AEIOUaeiou"
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print("Total de vogais:", contador)