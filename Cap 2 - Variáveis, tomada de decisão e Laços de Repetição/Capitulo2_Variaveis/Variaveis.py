nome = input("Digite o nome de um funcionario: ")
empresa = input("Digite a instituicao: ")
qtde_funcionarios = int(input("Digite a qtde de funcionarios: "))
mediaSalarial = float(input("Digite a média salarial: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcaionarios.")
print("A media da salarial é de: " + str(mediaSalarial))

print("==========Verifique os tipos de dados abaixo:==========")

print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaSalarial é ",type(mediaSalarial))