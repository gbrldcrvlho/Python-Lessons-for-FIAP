nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectoContagiosa = input("Suspeita de doenca infecto-contagiosa?").upper()

if idade >=65 and doenca_infectoContagiosa == "SIM":
    print("O paciente sera direcionado para a sala AMARELA - COM prioridade")
elif idade < 65 and doenca_infectoContagiosa == "SIM":
    print("O paciente sera direcionado para a sala AMARELA - SEM prioridade")
elif idade >=65 and doenca_infectoContagiosa == "NAO":
    print("O paciente sera direcionado para a sala BRANCA - COM PRIORIDADE")
elif idade < 65 and doenca_infectoContagiosa == "NAO":
    print("O paciente sera direcionado para a sala BRANCA - SEM PRIORIDADE")
else:
    print("Responda a suspeita de doenca infecto-contagiosa com SIM ou NAO")