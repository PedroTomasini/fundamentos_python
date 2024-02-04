def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Saque APROVADO!")
        print("Retire seu dinheirona boca do caixa.")
    elif saldo <= valor:
        print("Saldo insuficiente, tente outro valor.")

sacar(500)

    
