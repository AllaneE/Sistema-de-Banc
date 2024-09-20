menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True :
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor;
            extrato += f"Deposito de R$ {valor:.2f}\n"

        else:
            print("Valor inválido. Deposite valores maiores que 0")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= 3

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! Saque excede o valor limite. ")
        
        elif excedeu_saques:
            print("Operação falhou! Você excedeu a quatidade de saques.")

        elif valor> 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor inválido.")

    elif opcao == "e":
        print("\n      EXTRATO      ")
        print("Não há movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else: 
        print("Opção invalida, tente novamente!")

