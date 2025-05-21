numeros = []

for i in range(3):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

numeros_dobrados = [num * 2 for num in numeros]

print("Números originais:", numeros)
print("Números multiplicados por 2:", numeros_dobrados)

soma_original = sum(numeros)
print("Soma dos números originais:", soma_original)

soma_dobrada = sum(numeros_dobrados)
print("Soma dos números multiplicados por 2:", soma_dobrada)