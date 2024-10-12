def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor;
        extrato += f"Deposito de R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    else:
        print("Valor inválido. Deposite valores maiores que 0")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limites_saque):
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
    
    return saldo, extrato


def exibir_extrato(saldo,/,*,extrato):
    print("\n      EXTRATO      ")
    print("Não há movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    
def criar_usuario(usuarios):
    cpf = input("Informe seu CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe uma conta com esse CPF")
        return
    
    nome= input("Digite seu nome:")
    data_nascimento= input("informe sua data de nascimento:")
    endereco= input("Informe seu endereço")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco": endereco})
    print("Usuario criado com sucesso!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}

    return "Usuario não encontrado"

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios=[]
    contas=[]
    AGENCIA = "0001"

    while True :
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
        
            saldo,extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo,extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limites_saque=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "q":
            break

        else: 
            print("Opção invalida, tente novamente!")

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [Nu] Novo Usuário
    [q] Sair

    => """
    return input(menu)



main()