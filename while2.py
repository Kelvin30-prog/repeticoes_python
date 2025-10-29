# Solicitando que o usuário escreva alguma palavra
# Para finalizar terá que escrever 'sair'
palavra = ""

# Atribuindo repetição
while palavra.lower() != "sair":
    palavra = (input("Digite uma palavra: "))

else:
    print("")
    print("Programa encerrado.")