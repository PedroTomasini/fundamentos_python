nome = "peDro"

print(nome.upper())  #PEDRO
print(nome.lower())  #pedro
print(nome.title())  #Pedro

texto = "    Olá, mundo!    "

print(texto.strip())   # "Olá, mundo!"
print(texto.lstrip())  # "Olá, mundo!"
print(texto.rstrip())  # "    Olá, mundo!"

menu = "Python"

print("####" + menu + "####")  # ####Python####
print(menu.center(14))         #    Python   
print(menu.center(14, "*"))    # ****Python****
print("-".join(menu))          # -Python- 