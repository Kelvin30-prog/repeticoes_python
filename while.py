# Solicitando ao usuário que digite um número dentro dos padrões estabelecidos.
numero = 1

# Atribuindo repetição
while numero > 0 and numero < 100:
    numero = int(input("Digite um número maior que zero e menor que cem: "))

else:
    print("")
    print("Número inválido! Sistema encerrado.")