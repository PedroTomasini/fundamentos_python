nome = "Pedro"
idade = 33
profissao = "Programador"
linguagem = "Python"
saldo = 45.97

dados = {"nome": "Pedro", "idade": 33} 

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))

print("Nome: {0} Idade: {1} Nome: {1} {1}" .format(nome, idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:0.2f}")
