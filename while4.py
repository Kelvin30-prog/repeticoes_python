# Este sistema demonstra várias opções ao usuário e solicita uma escolha dele
# Apresentando opções de escolha
print("Escolha uma das opções abaixo:")
print("Opção 1")
print("Opção 2")
print("Opção 3")
print("Opção 4")
print("Opção 5")
print("")

# Solicitando sua escolha
escolha = int(input("Digite o número da opção escolhida: "))

# Atribuindo repetições
while escolha >= 1 and escolha <=5:
    if escolha == 1:
        print("Você escolheu a opção 1")
    elif escolha == 2:
        print("Você escolheu a opção 2")
    elif escolha == 3:
        print("Você escolheu a opção 3")
    elif escolha == 4:
        print("Você escolheu a opção 4")
    elif escolha == 5:
        print("Você escolheu a opção 5")
    print("")
    escolha = int(input("Digite o número da opção escolhida: "))

# Mensagem ao usuário caso ele escolha uma opção que não foi fornecida
else:
    print("OPÇÃO INVÁLIDA")
    print("PROGRAMA ENCERRADO")