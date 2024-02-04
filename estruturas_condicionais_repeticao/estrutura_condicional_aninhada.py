conta_normal = False
conta_universitaria = True
conta_especial = False

saldo = 2000
cheque_especial = 450
saque = 2400

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")

elif conta_especial:
    print("Conta especial selecionada.")
else:
    print("Conta não encontrada.")
