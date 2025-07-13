def exibir_cabecalho():
    print('=' * 30)
    print(" QUEREMOS SABER SUA OPINIÃO ")
    print('=' * 30)


def solicitar_idade():
    while True:
        try:
            idade = int(input("Informe sua idade (ou 0 para sair): "))
            if idade < 0:
                print("Idade inválida. Tente novamente.")
            else:
                return idade
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


def solicitar_avaliacao():
    while True:
        try:
            print("[1] Satisfatório  [2] Indiferente  [3] Insatisfatório")
            opcao = int(input("Sua avaliação: "))
            if opcao in [1, 2, 3]:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")


def calcular_media(soma, quantidade):
    return soma / quantidade if quantidade > 0 else 0


def exibir_resultados(total, satisfatorio, indiferente, insatisfatorio, media_geral, media_satisfatorio):
    print('\n' + '=' * 30)
    print("        RESULTADOS FINAIS       ")
    print('=' * 30)
    print(f"Total de avaliações: {total}")
    print(f"Responderam Satisfatório: {satisfatorio}")
    print(f"Responderam Indiferente: {indiferente}")
    print(f"Responderam Insatisfatório: {insatisfatorio}")
    print(f"Média de idade geral: {media_geral:.2f}")
    print(f"Média de idade (Satisfatório): {media_satisfatorio:.2f}")


def executar_pesquisa():
    total_idade = 0
    contador = 0
    satisfatorio = indiferente = insatisfatorio = 0
    soma_idade_satisfatorio = cont_satisfatorio = 0

    exibir_cabecalho()

    while True:
        idade = solicitar_idade()
        if idade == 0:
            break

        total_idade += idade
        contador += 1

        avaliacao = solicitar_avaliacao()

        if avaliacao == 1:
            satisfatorio += 1
            soma_idade_satisfatorio += idade
            cont_satisfatorio += 1
        elif avaliacao == 2:
            indiferente += 1
        elif avaliacao == 3:
            insatisfatorio += 1

    media_geral = calcular_media(total_idade, contador)
    media_satisfatorio = calcular_media(soma_idade_satisfatorio, cont_satisfatorio)

    exibir_resultados(
        contador,
        satisfatorio,
        indiferente,
        insatisfatorio,
        media_geral,
        media_satisfatorio
    )


# Inicia o programa
executar_pesquisa()
