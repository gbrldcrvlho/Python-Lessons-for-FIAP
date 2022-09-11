nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doenca_infectoContagiosa = input("Suspeita de doença Infecto-Contagiosa? Responda com VERDADEIRO ou FALSO: ").upper()
resposta = "SIM"

# PRIMEIRO PROBLEMA A SER RESOLVIDO

while resposta == "SIM":
    if doenca_infectoContagiosa == "VERDADEIRO":
        print("Encaminhe o paciente para a sala AMARELA.")
    elif doenca_infectoContagiosa == "FALSO":
        print("Encaminhe o paciente para a sala BRANCA.")
    else:
        print("Responda a suspeita de doença Infecto-Contagiosa com VERDADEIRO ou FALSO! ").upper()

# SEGUNDO PROBLEMA A SER RESOLVIDO
    if idade >= 65:
        print("Paciente COM prioridade!")
    else:
        genero = input("Digite o genero do paciente: ").upper()
        if genero == "FEMININO" and idade > 10:
            gravidez = input("A paciente esta gravida? Responda com VERDADEIRO ou FALSO: ").upper()
            if gravidez == "VERDADEIRO":
                print("Paciente COM prioridade!")
            elif gravidez == "FALSO":
                print("Paciente SEM prioridade!")
else:
    resposta = input("Deseja adicionar mais um paciente a fila de espera? ").upper()

