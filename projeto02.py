#Checar redundância

class Titular:

    def __init__(self):
        self.nome = ""
        self.numero_conta = ""
        self.saldo = 0

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_numero_conta(self):
        return self.numero_conta

    def set_numero_conta(self, numero_conta):
        self.numero_conta = numero_conta

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

class ContaBancaria:

    def __init__(self):
        self.titular = None

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def depositar(self, quantidade):
        self.titular.saldo += quantidade
        print("Deposito de R$",quantidade,"realizado com sucesso na conta",self.titular.numero_conta,
              "| Saldo atual:",self.titular.saldo)

    def sacar(self, quantidade):
        if self.titular.saldo < quantidade:
            print("Tentativa de saque de R$",quantidade,"falhou : SALDO INSUFICIENTE.")
        else:
            self.titular.saldo -= quantidade
            print("Saque de R$", quantidade,"realizado com sucesso na conta",self.titular.numero_conta,
                  "| Saldo atual:",self.titular.saldo)

    def get_nome_titular(self):
        if self.titular is None:
            print("Titular não definido")
        if self.titular.numero_conta is None:
            print("Conta inexistente")
        else:
            return self.titular.get_nome()

    def get_numero_conta(self):
        return self.titular.get_numero_conta()

    def get_saldo(self):
        return f"R$ {self.titular.saldo:,.2f}".replace(",","X").replace(".",",").replace("X",".")

    def get_dados(self):
        if self.titular is None or self.titular.numero_conta == "" or self.titular.nome == "":
            return f"Conta inexistente"
        else:
            return f"| {self.titular.get_nome()} | {self.titular.get_numero_conta()} |"


titular0 = Titular()
titular0.set_nome("Boris")
titular0.set_numero_conta("100800-8")
titular0.set_saldo(10000)

conta0 = ContaBancaria()
conta0.set_titular(titular0)
print(conta0.get_dados())
print(conta0.get_saldo())
conta0.sacar(2500)
conta0.depositar(800)
conta0.sacar(8500)

print()

titular1 = Titular()
titular1.set_nome("Gragas")
titular1.set_numero_conta("100801-8")
titular1.set_saldo(40)

conta1 = ContaBancaria()
conta1.set_titular(titular1)
print(conta1.get_dados())
print(conta1.get_saldo())
conta1.sacar(50)
