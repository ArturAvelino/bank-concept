from utils.helper import formata_valor


class Conta:

    contador = 1000

    def __init__(self, titular, saldo):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = int(saldo)
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    def saque(self, valor):
        self.__saldo -= valor

    def deposito(self, valor):
        self.__saldo += valor

    def transferencia(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor


    def __str__(self):
        return f"Número da conta: {self.numero} \nTitular: {self.titular} \nSaldo: {formata_valor(self.saldo)}"
