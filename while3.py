# Pergunta ao usuário se ele deseja continuar a operação
pergunta = (input("Deseja continuar a operação? (responda 'sim' ou 'não'): "))

# Atribuindo repetição
while pergunta.lower() == "sim":
    pergunta = (input("Deseja continuar a operação? (responda 'sim' ou 'não'): "))

else:
    print("")
    print("Programa encerrado.")