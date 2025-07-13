salario_funcionario = float(input("Informe o salário do Funcionário: "))
codigo_cargo = int(input("Informe o código do cargo: [1] Servente [2] Pedreiro [3] Mestre de Obras [4] Técnico de Segurança: "))

if codigo_cargo == 1:
    novo_salario = salario_funcionario + (salario_funcionario * 40/100)
    print("Novo salário: ", novo_salario)
elif codigo_cargo == 2:
    novo_salario = salario_funcionario + (salario_funcionario * 35/100)
    print("Novo salário: ", novo_salario)
elif codigo_cargo == 3:
    novo_salario = salario_funcionario + (salario_funcionario * 20/100)
    print("Novo salário: ", novo_salario)
elif codigo_cargo == 4:
    novo_salario = salario_funcionario + (salario_funcionario * 10/100)
    print("Novo salário: ", novo_salario)
else:
    print("Código Inválido!")