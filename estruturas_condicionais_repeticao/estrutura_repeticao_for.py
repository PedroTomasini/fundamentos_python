texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

# Exemplo utulizando iterável.
for letra in texto:
    if letra.upper()in VOGAIS:
        print(letra, end="")
else:
    print()

# Exemplo utulizando a função buind-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")





