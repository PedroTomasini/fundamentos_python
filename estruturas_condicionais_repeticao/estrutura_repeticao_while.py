opcao = -1

while opcao!= 0:
    opcao = int(input("[1] Sacar \n[2] Depositar \n[0] Sair \n: "))

    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2: 
        print("Depósito realizado com sucesso!")
    else:
        print("Obrigado por usar nosso sistema bancário, até logo!")