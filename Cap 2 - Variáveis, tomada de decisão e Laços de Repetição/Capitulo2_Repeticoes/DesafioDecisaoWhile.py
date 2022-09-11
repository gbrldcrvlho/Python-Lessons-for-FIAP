resposta = "SIM"
while resposta =="SIM":
    nivel = input("Digite o nivel de acesso: ").upper()
    if nivel == "ADM" or nivel == "USR":
        genero = input("Digite o seu genero: ").upper()
        if nivel == "ADM":
            if genero == "FEMININO":
                print("Olá Administradora!")
            else:
                print("Olá Administrador")
        else:
            if genero == "FEMININO":
                print("Olá Usuária!")
            else:
                print("Olá Usuário!")
    elif nivel == "GUEST":
        print("Olá Visitante!")
    else:
        print("Olá Desconhecido(a)!")
    resposta = input("Digite SIM para continuar: ").upper()