class ContaBancaria:
    titular = ""
    numero_conta = ""
    saldo = 0

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_numero_conta(self):
        return self.numero_conta

    def set_numero_conta(self, numero_conta):
        self.numero_conta = numero_conta

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def depositar(self, quantidade):
        self.saldo += quantidade
        print("Deposito de R$",quantidade,"realizado com sucesso na conta",self.numero_conta,
              "| Saldo atual:",self.saldo)

    def sacar(self, quantidade):
        if self.saldo < quantidade:
            print("Tentativa de saque de R$",
                  quantidade,
                  "falhou : SALDO INSUFICIENTE.")
        else:
            self.saldo -= quantidade
            print("Saque de R$", quantidade,"realizado com sucesso na conta",self.numero_conta,
                  "| Saldo atual:",self.saldo)


conta1 = ContaBancaria()
conta1.titular = "Boris"
conta1.numero_conta = "234567-8"
conta1.saldo = 10000
print(conta1.titular)
print(conta1.numero_conta)
print(conta1.saldo)
conta1.depositar(2000)
conta1.sacar(4000)
conta1.sacar(10000)