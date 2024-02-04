MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:   
    print("Você é maior de idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("Você ainda não pode tirar CNH.")


if idade >= MAIOR_IDADE:   
    print("Você é maior de idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Você pode fazer as aulas teóricas, mas não pode fazer as aulas práticas.")
else:
    print("Você ainda não pode tirar CNH.")