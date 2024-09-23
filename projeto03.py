class Pessoa:
    nome = ""
    idade = 0
    altura = 0
    peso = 0.0

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_altura(self):
        return self.altura

    def set_altura(self, cm):
        self.altura = cm

    def get_peso(self):
        return self.peso

    def set_peso(self, kg):
        self.peso = kg

    def exibir_dados(self):
        print(self.nome,"|",self.idade,"anos","|",self.altura,"cm","|",self.peso,"Kg")

    def envelhecer(self, anos):
        self.idade += anos
        print(self.nome,"envelheceu",anos,"anos")

    def crescer(self, cm):
        if self.idade < 21:
            self.altura += cm
            print(self.nome,"cresceu",cm,"centímetros")
        else:
            print(self.nome,"não cresce mais")

    def ganhar_peso(self, kg):
        self.peso += kg
        print(self.nome,"ganhou",kg,"Kg")

    def perder_peso(self, kg):
        self.peso -= kg
        print(self.nome,"perdeu",kg,"Kg")



pessoa1 = Pessoa()
pessoa1.nome = "Matheus"
pessoa1.idade = 10
pessoa1.altura = 158
pessoa1.peso = 71.2
pessoa1.exibir_dados()
pessoa1.envelhecer(4)
pessoa1.crescer(12)
pessoa1.ganhar_peso(6.3)
pessoa1.exibir_dados()
pessoa1.envelhecer(6)
pessoa1.crescer(9)
pessoa1.perder_peso(5.1)
pessoa1.exibir_dados()
pessoa1.envelhecer(2)
pessoa1.crescer(6)
pessoa1.perder_peso(2.2)
pessoa1.exibir_dados()