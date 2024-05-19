def main():
    menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Criar Usuario
    [nc] Criar Conta
    [q] Sair
    
    => """
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
    
        opcao = input(menu)
    
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato =  depositar(valor, saldo, extrato)
        
        elif opcao == "s":
           valor = float(input("Informe o valor: "))
           saldo, extrato = sacar(
                valor=valor, 
                saldo=saldo, 
                extrato=extrato, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES, 
                limite=limite)
    
        elif opcao == "e":
            ver_extrato(saldo, extrato=extrato)
    
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "q":
            break
    
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso")
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, valor, saldo, extrato, numero_saques, limite_saques, limite):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Digite o seu cpf(apenas números)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Este usuário já existe")
        return
    nome = input("Digite o seu nome")
    data_de_nascimento = input("Digite a sua data de nascimento: {00/00/0000}")
    endereco = input("Digite o seu endereço: {Bairro, Rua, Número}")
    usuarios.append({"nome": nome, "cpf": cpf, "data_de_nascimento": data_de_nascimento, "endereco": endereco})
    print("Usuario criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario[cpf] == usuario:
            return True
        
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o seu cpf(apenas números)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario não encontrado")


main()
