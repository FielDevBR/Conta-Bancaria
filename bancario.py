saldo= 23 #numero Inteiro


#Opções do Menu
print("Bem-vindo a sua conta bancaria!")
print("Por favor, escolha uma opção:")
print("1. Transferir")
print("2. Depositar")
print("3. Retirar")
#escolha
escolha = input("Digite o número correspondente à sua escolha: ")

if escolha == "1":
    transferencia = int(input("Digite O Valor Da Transferencia: "))
    saldo -= transferencia  # Adiciona o valor da transferência ao saldo
    print("Transferência realizada com sucesso. Seu novo saldo é:", saldo)
elif escolha == "2":
    deposito = int(input("Digite O Valor Do Deposito: "))
    saldo += deposito  # Adiciona o valor da transferência ao saldo
    print("Deposito realizado com sucesso. Seu novo saldo é:", saldo)
elif escolha == "3":
    retirada = int(input("Digite o Valor Da Retirada: "))  
    if saldo < retirada:
        print("Saldo Insuficiente, Tente Novamente!")
    else:
        saldo -= retirada
        print("Retirada realizada com sucesso. Seu novo saldo é:", saldo)
else:
    print("Opção inválida. Por favor, escolha um número válido.")