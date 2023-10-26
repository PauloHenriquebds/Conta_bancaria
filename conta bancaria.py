from biblioteca import ContaBancaria

conta = ContaBancaria("Paulo", 0, 123321, "Corrente", 800, False)

conta.ativarconta()
conta.depositar()
conta.sacar()
conta.ativarconta()
conta.verificarsaldo()
