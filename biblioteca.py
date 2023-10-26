class ContaBancaria:
    def __init__(self, nome, saldo, numero, tipo, limite, status = False):
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.numero = numero
        self.status = status
        self.limite = limite

    def depositar(self):
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito > 0:
            self.saldo += deposito
            print(f"Saldo atual: R${self.saldo}")
        else:
            print("Deposito invalido")
    def sacar(self):
        print(f"Seu limite para saque é: R${self.limite}")
        saque = float(input("Digite o valor do saque: "))
        if saque > 0 and saque <= self.saldo and saque <= self.limite:
            self.saldo -= saque
            print(f"Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente")
    def ativarconta(self):
        if self.status == False:
            self.status = True
            print("Conta ativa")
        else:
            print("Está conta já está ativa")
    def verificarsaldo(self):
        print(f"Saldo atual {self.saldo}")