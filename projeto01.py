class Marca:
    def __init__(self):
        self.nome = ""

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

class Modelo:
    def __init__(self):
        self.nome = ""

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

class Carro:

    def __init__(self):
        self.marca = None
        self.modelo = None
        self.ano = 0
        self.velocidade_atual = 0
        self.ligado = False

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
        return f"{self.velocidade_atual} Km/h"

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
            print(self.get_nome_marca(),self.get_nome_modelo(),"ligado.")
        else:
            print("Este", self.get_nome_modelo(), "ja esta ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade_atual = 0
            print(self.get_nome_marca(),self.get_nome_modelo(), "desligado.")
        else:
            print("Este", self.get_nome_modelo(),"ja esta desligado.")

    def frear(self, quantidade):
        if not self.ligado:
            print(self.get_nome_modelo(), "desligado, impossivel frear.")
        else:
            if quantidade > self.velocidade_atual:
                print("Frenagem invalida")
            else:
                self.velocidade_atual -= quantidade

    def get_nome_marca(self):
        if self.marca is None:
            print("Carro sem marca definida")
        else:
            return self.marca.get_nome()

    def get_nome_modelo(self):
        if self.modelo is None:
            print("Carro sem modelo definido")
        else:
            return self.modelo.get_nome()

marca0 = Marca()
marca0.set_nome("Fiat")

modelo0 = Modelo()
modelo0.set_nome("Marea")

carro0 = Carro()
carro0.set_marca(marca0)
carro0.set_modelo(modelo0)
print(carro0.get_nome_marca())
print(carro0.get_nome_modelo())
carro0.ligar()
carro0.acelerar(40)
carro0.acelerar(20)
print(carro0.get_velocidade_atual())
carro0.frear(30)
print(carro0.get_velocidade_atual())
carro0.frear(30)
print(carro0.get_velocidade_atual())
carro0.desligar()
print()

marca1 = Marca()
marca1.set_nome("Koenigsegg")

modelo1 = Modelo()
modelo1.set_nome("Jesko")

carro1 = Carro ()
carro1.set_marca(marca1)
carro1.set_modelo(modelo1)
print(carro1.get_nome_marca())
print(carro1.get_nome_modelo())
carro1.ligar()
carro1.acelerar(110)
carro1.acelerar(50)
print(carro1.get_velocidade_atual())
carro1.frear(90)
print(carro1.get_velocidade_atual())
carro1.frear(70)
print(carro1.get_velocidade_atual())
carro1.desligar()
carro1.frear(30)
