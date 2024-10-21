class Pais:

    def __init__(self):
        self.sede = ""

    def get_sede(self):
        return self.sede

    def set_sede(self, sede):
        self.sede = sede

class Estado:

    def __init__(self):
        self.estado = ""

    def get_nome(self):
        return self.estado

    def set_nome(self, estado):
        self.estado = estado

class Filial:

    def __init__(self, estado):
        self.filial = ""
        self.estado = estado

    def get_nome(self):
        return self.filial

    def set_nome(self, filial):
        self.filial = filial

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        if self.estado is None:
            print("Filial sem estado definido")
        else:
            self.estado = estado

    def get_nome_estado(self):
            return self.estado.get_nome()

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

    def __init__(self, escolaridade, pais, filial):
        self.nome = ""
        self.empresa = None
        self.set_escolaridade(escolaridade)
        self.set_pais(pais)
        self.set_filial(filial)

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
            print("Funcionario sem país definido")
            exit()
        self.pais = pais

    def get_alocacao_pais(self):
        return self.pais.get_sede()

    def get_filial(self):
        return self.get_filial()

    def set_filial(self, filial):
        self.get_filial = filial

class Departamento:

    def __init__(self, chefe):
        self.departamento = ""
        self.set_chefe(chefe)

    def get_departamento(self):
        return self.departamento

    def set_departamento(self, departamento):
        self.departamento = departamento

    def get_chefe(self):
        return self.chefe

    def set_chefe(self, chefe):
        self.chefe = chefe

    def get_nome_chefe(self):
        if self.chefe is None:
            print(f"Sem chefe de departamento definido para: {self.get_departamento()}")
        else:
            return self.get_chefe

class Empresa:

    def __init__(self, diretor, filial):
        self.nome = ""
        self.set_diretor(diretor)
        self.set_filial(filial)

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_diretor(self):
        return self.set_diretor

    def set_diretor(self, diretor):
        self.diretor = diretor

    def get_filial(self):
        return self.set_filial

    def set_filial(self, filial):
        self.get_filial = filial

    def get_nome_filial(self):
        if self.set_filial is None:
            print("Empresa sem filial definida")
            exit()
        else:
            return self.get_filial


class Escolaridade:

    def __init__(self):
        self.nome = ""

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome


escolaridade1 = Escolaridade()
escolaridade1.set_nome("Mestrado")
escolaridade2 = Escolaridade()
escolaridade2.set_nome("Especialização")

pais1 = Pais()
pais1.set_sede("Brasil")

estado1 = Estado()
estado1.set_nome("Minas Gerais")

filial1 = Filial(estado1)
filial1.set_nome("Juiz de Fora")

funcionario1 = Funcionario(escolaridade1, pais1, filial1)
funcionario1.nome = "João"
funcionario2 = Funcionario(escolaridade2, pais1, filial1)
funcionario2.nome = "Maria"
funcionario3 = Funcionario(escolaridade1, pais1, filial1)

departamento1 = Departamento(funcionario2)
departamento1.set_departamento("Gestão de Riscos")

empresa1 = Empresa(funcionario3, filial1)
empresa1.nome = "VASP"

grupo1 = Grupo()
grupo1.set_presidente(funcionario1)

print(f"Escolaridade do presidente do grupo: {grupo1.get_nome_escolaridade_presidente()}")
print(f"País de alocação do funcionário: {funcionario1.get_alocacao_pais()}")
print(f"Estado de alocação da filial coordenada pelo funcionário: {filial1.get_nome_estado()}")
print(f"Escolaridade do chefe do departamento de {departamento1.get_departamento()}: {funcionario2.get_nome_escolaridade()}")
print(f"Nome do diretor da empresa {empresa1.get_nome()}, da filial de {empresa1.get_nome_filial()}")