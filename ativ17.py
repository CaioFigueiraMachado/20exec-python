# Solicita ao usuário um número de 1 a 7
numero = int(input("Digite um número de 1 a 7: "))

dias_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

dia = dias_semana.get(numero, "Número inválido. Digite um número de 1 a 7.")
print(dia)