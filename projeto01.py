class Carro:
    marca = ""
    modelo = ""
    ano = 0
    velocidade_atual = 0
    estado = "desligado"

    def ligar(self):
        self.estado = "ligado"

    def desligar(self):
        self.estado = "desligado"

carro = Carro()
carro.marca = "Fiat"
carro.modelo = "Marea"
print(carro.marca)
carro.ligar()
print(carro.estado)
carro.desligar()
print(carro.estado)

carro1 = Carro ()
carro1.marca = "Peugeot"
carro1.modelo = "206"
print(carro1.marca)
carro1.ligar()
print(carro1.estado)
carro1.desligar()
print(carro1.estado)
