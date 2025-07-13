from datetime import date

def voto(ano):
    ano_atual = date.today().year
    idade = ano_atual - ano
    
    if ano > date.today().year:
        return "ANO INVÁLIDO"
    elif idade < 16:
        return "NEGADO"
    elif 16 <= idade <= 17 or idade >= 65:
        return "OPCIONAL"
    elif 18 <= idade <= 64:
        return "OBRIGATÓRIO"

#Programa Principal
nasc = int(input("Ano de nascimento: "))
tipo_voto = voto(nasc)
idade = date.today().year - nasc
print(f"Com {idade} anos: VOTO {tipo_voto}")
