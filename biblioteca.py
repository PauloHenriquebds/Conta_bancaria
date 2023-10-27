class ContaBancaria:
    def __init__(self, nome, numero, tipo, status = False):
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.numero = numero
        self.status = status
        self.limiteCont = False
        self.zerar = 0
        self.limite = 0

    def depositar(self):
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito >= 0:
            self.saldo += deposito
            print(f"Saldo atual: R${self.saldo}")
        else:
            print("Deposito invalido")
    def sacar(self):
        print(f"Seu limite para saque é: R${self.limite}")
        saque = float(input("Digite o valor do saque: "))
        if saque > 0 and saque <= self.saldo:
            self.saldo -= saque
            print(f"Saldo atual: R${self.saldo}")
        else:
            self.zerar += saque
            saque -= self.saldo
            self.saldo -= self.zerar
            print(f"Iremos retirar: R${saque} do seu limite")
            if saque <= self.limite:
                self.limite -= saque
                print(f"Seu limite agora é: R${self.limite}")
            else:
                print("Limite insuficiente")
    def ativarconta(self):
        if self.status == False:
            self.status = True
            print("Conta ativa")
        else:
            print("Está conta já está ativa")
    def verificarsaldo(self):
        if self.saldo < 0:
            self.saldo = 0
            print(f"Saldo atual: R${self.saldo}")
        else:
            print(f"Saldo atual: R${self.saldo}")
    def ativarlimite(self):
        if self.limiteCont == False:
            self.limiteCont = True
            self.limite = float(input("Qual o valor do limite?: "))
        else:
            print("Está conta já está ativa")
