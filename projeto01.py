class Carro:
    marca = ""
    modelo = ""
    ano = 0
    velocidade_atual = 0
    ligado = False

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_ano(self):
        return self.ano

    def set_ano(self, ano):
        if ano < 0:
            print("Ano inválido.")
        else:
            self.ano = ano

    def get_velocidade_atual(self):
        return self.velocidade_atual

    def set_velocidade_atual(self, velocidade_atual):
        if velocidade_atual < 0:
            print("Velocidade não pode ser menor que 0.")
        else:
            self.velocidade_atual = velocidade_atual

    def get_ligado(self):
        return self.ligado

    def set_ligado(self, ligado):
        self.ligado = ligado

    def acelerar(self, quantidade):
        if self.ligado:
            self.velocidade_atual += quantidade
        else:
            print("Não é possível acelerar o carro desligado.")

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(self.modelo,"ligado.")
        else:
            print("Este", self.modelo, "ja esta ligado.")


    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade_atual = 0
            print(self.modelo, "desligado.")
        else:
            print("Este", self.modelo,"ja esta desligado.")

    def frear(self, quantidade):
        if self.ligado == False:
            print(self.modelo, "desligado, impossivel frear.")
        else:
            if quantidade > self.velocidade_atual:
                print("Frenagem invalida")
            else:
                self.velocidade_atual -= quantidade


carro0 = Carro()
carro0.marca = "Fiat"
carro0.modelo = "Marea"
print(carro0.marca)
print(carro0.modelo)
carro0.ligar()
carro0.acelerar(40)
carro0.acelerar(20)
print(carro0.velocidade_atual)
carro0.frear(30)
print(carro0.velocidade_atual)
carro0.frear(30)
print(carro0.velocidade_atual)
carro0.desligar()

carro1 = Carro ()
carro1.marca = "Peugeot"
carro1.modelo = "206"
print(carro1.marca)
print(carro1.modelo)
carro1.ligar()
carro1.acelerar(70)
carro1.acelerar(20)
print(carro1.velocidade_atual)
carro1.frear(50)
print(carro1.velocidade_atual)
carro1.frear(40)
print(carro1.velocidade_atual)
carro1.desligar()
