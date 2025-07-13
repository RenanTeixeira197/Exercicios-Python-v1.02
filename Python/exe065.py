# Deve ser permitido executar quantas consultas forem necessárias
# e o programa deve ser encerrado quando o usuário digitar 'sair'.
# O programa deve exibir os dados do funcionário cadastrado.
# File: exe064.py


funcionarios = {
    'matricula': 0.0,
    'nome': '',
    'setor': '',
    'salario': 0.0,
}

def cadastrar_funcionario(funcionarios):
    for i in range(4):
        print(f"\nCadastro do Funcionário {i + 1}:")
        funcionarios['matricula'] = int(input("Digite a matrícula do funcionário: "))
        funcionarios['nome'] = input("Digite o nome do funcionário: ")
        funcionarios['setor'] = input("Digite o setor do funcionário: ")
        funcionarios['salario'] = float(input("Digite o salário do funcionário: "))


def exibir_funcionario(funcionarios):
    print("\nDados do Funcionário:")
    print(f"Matrícula: {funcionarios['matricula']}")
    print(f"Nome: {funcionarios['nome']}")
    print(f"Setor: {funcionarios['setor']}")
    print(f"Salário: R$ {funcionarios['salario']:.2f}")


def main():
    cadastrar_funcionario(funcionarios)
    exibir_funcionario(funcionarios)

if __name__ == "__main__":
    main()

