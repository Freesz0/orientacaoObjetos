class Funcionario:

    nome = ""
    cargo = ""
    salario = 0.0
    departamento = ""
    BREAK = "////////"
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def receber_aumento(self, aumento):
        self.salario += self.salario * aumento/100

    def mudar_departamento(self, novo_departamento):
        if novo_departamento == self.departamento:
            print("Não foi possivel mudar",self.nome,"de departamento: ja esta alocado em",novo_departamento)
        else:
            self.departamento = novo_departamento
            print(self.nome,"foi realocado de departamento:",novo_departamento)

    def mudar_cargo(self, novo_cargo):
        if novo_cargo == self.cargo:
            print(self.nome,"ja e",novo_cargo)
        else:
            self.cargo = novo_cargo
            print(self.nome,"teve o cargo alterado para:",novo_cargo)

    def exibir_dados(self):
        print("|",self.nome,"|",self.cargo,"|",self.salario,"|",self.departamento,"|")

funcionario1 = Funcionario()
funcionario1.nome = "Michael"
funcionario1.cargo = "Gerente Regional"
funcionario1.salario = 15000
funcionario1.departamento = "Administracao"
funcionario1.exibir_dados()
funcionario1.mudar_departamento("Administracao")
funcionario1.exibir_dados()

funcionario2 = Funcionario()
funcionario2.nome = "Jim"
funcionario2.cargo = "Vendedor"
funcionario2.salario = 4000
funcionario2.departamento = "Vendas"
funcionario2.exibir_dados()
funcionario2.mudar_departamento("Administracao")
funcionario2.mudar_cargo("Gestor de Vendas")
funcionario2.receber_aumento(20)
funcionario2.exibir_dados()


