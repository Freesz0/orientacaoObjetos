class Pais:
    def __init__(self):
        self.sede = ""
    def get_sede(self):
        return self.sede
    def set_sede(self, sede):
        self.sede = sede

class Grupo:
    def __init__(self):
        self.presidente = None
    def get_presidente(self):
        return self.presidente
    def set_presidente(self, presidente):
        self.presidente = presidente
    def get_nome_escolaridade_presidente(self):
        if self.presidente is None:
            print("Grupo sem presidente")
        else:
            return self.presidente.get_nome_escolaridade()

class Funcionario:
    def __init__(self, escolaridade, pais):
        self.set_escolaridade(escolaridade)
        self.set_pais(pais)
    def get_escolaridade(self):
        return self.escolaridade
    def set_escolaridade(self, escolaridade):
        if escolaridade is None:
            print("Funcionario sem escolaridade definida")
            exit()
        self.escolaridade = escolaridade
    def get_nome_escolaridade(self):
        return self.escolaridade.get_nome()
    def get_pais(self):
        return self.pais
    def set_pais(self, pais):
        if pais is None:
            print("Funcionario sem Pais definido")
            exit()
        self.pais = pais

class Escolaridade:
    def __init__(self):
        self.nome = ""
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome


escolaridade1 = Escolaridade()
escolaridade1.set_nome("Graduacao")

pais1 = Pais()
pais1.set_sede("Brasil")

funcionario1 = Funcionario(escolaridade1, pais1)

grupo1 = Grupo()
grupo1.set_presidente(funcionario1)

print(grupo1.get_nome_escolaridade_presidente())