from time import sleep
from utils.helper import formata_valor
from models.contas import Conta


contas = []


def main():
    menu()


def menu():
    print("================================================================")
    print("======================== Bem-vindo(a)! =========================")
    print("========================= Tuca's Bank ==========================")
    print("================================================================\n")
    print("Selecione uma opção abaixo: ")
    print("1 - Criar conta")
    print("2 - Efetuar saque")
    print("3 - Efetuar depósito")
    print("4 - Efetuar transferência")
    print("5 - Listar contas")
    print("6 - Sair")

    escolha = int(input("O que deseja fazer? "))

    if escolha == 1:
        criar_conta()
    elif escolha == 2:
        efetuar_saque()
    elif escolha == 3:
        efetuar_deposito()
    elif escolha == 4:
        efetuar_transferencia()
    elif escolha == 5:
        listar_contas()
    else:
        print("Obrigado! Volte sempre.")
        sleep(3)
        exit()


def criar_conta():
    print("Cadastro de conta")
    print("====================")
    nome = input("Digite o nome do titular: ")
    saldo = input("Digite o saldo inicial: ")
    conta = Conta(nome, saldo)
    p = None
    for each in contas:
        if each.titular == nome:
            p = each.titular
    if p == conta.titular:
        print("O titular já possui uma conta")
        sleep(2)
        menu()
    else:
        contas.append(conta)
        print(f"A conta do titular {nome} foi cadastrado com sucesso!")
        sleep(2)
        menu()


def efetuar_saque():
    if len(contas) > 0:
        print("Listagem de contas")
        print("==================")
        for n in contas:
            print(f"{n} \n")
        numero_conta = int(input("Insira o número da conta que deseja sacar: "))
        conta = pega_conta_numero(numero_conta)
        print(f"O saldo da sua conta atualmente é: {formata_valor(conta.saldo)}")
        valor = int(input("Insira o valor que deseja sacar: "))
        if valor <= conta.saldo:
            if valor > 0:
                conta.saque(valor)
                print(f"Saque efetuado com sucesso \nSeu saldo atual é: {formata_valor(conta.saldo)}")
                print("Volte sempre!")
                sleep(3)
                menu()
            else:
                print("O valor para saque precisa ser positivo! ")
                sleep(2)
                menu()
        else:
            print("Valor insuficiente para saque")
            sleep(2)
            menu()


def efetuar_deposito():
    if len(contas) > 0:
        print("Listagem de contas")
        print("==================")
        for n in contas:
            print(f"{n} \n")
            sleep(1)
        sleep(2)
        numero_conta = int(input("Insira o número da conta que deseja depositar: "))
        conta = pega_conta_numero(numero_conta)
        print(f"O saldo da sua conta atualmente é: {formata_valor(conta.saldo)}")
        valor = int(input("Insira o valor que deseja depositar: "))
        if valor > 0:
            conta.deposito(valor)
            print(f"Depósito efetuado com sucesso! \nSeu saldo atual é: {formata_valor(conta.saldo)}")
            print("Volte sempre!")
            sleep(3)
            menu()
        else:
            print("O valor para depósito precisa ser positivo! ")
            sleep(2)
            menu()


def efetuar_transferencia():
    if len(contas) > 1:
        print("Listagem de contas")
        print("==================")
        for n in contas:
            print(f"{n} \n")
        numero_conta_1 = int(input("Insira o seu número de conta: "))
        conta1 = pega_conta_numero(numero_conta_1)
        print(f"Saldo na conta: {formata_valor(conta1.saldo)}")
        numero_conta_2 = int(input("Insira o número da conta que você deseja transferir: "))
        conta2 = pega_conta_numero(numero_conta_2)
        valor = int(input("Insira o valor que deseja transferir: "))
        if valor < conta1.saldo:
            if valor > 0:
                conta1.transferencia(valor, conta2)
                print("Transferência realizada com sucesso!")
                print(f"Títular {conta1.titular}({conta1.numero}) transferiu {formata_valor(valor)} para "
                      f"{conta2.titular}({conta2.numero})")
                sleep(5)
                menu()
            else:
                print(f"O valor para transferência precisa ser positivo! \n Tente novamente com um novo valor")
                sleep(2)
                menu()
        else:
            print("Valor insuficiente para realizar transferência \nTente novamente com um novo valor")


def listar_contas():
    if len(contas) > 0:
        print("Listagem de contas")
        print("==================")
        for n in contas:
            print(f"{n} \n")
    sleep(3)
    menu()


def pega_conta_numero(numero):
    p = None
    for each in contas:
        if each.numero == numero:
            p = each
    return p


if __name__ == "__main__":
    main()
