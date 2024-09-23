class Produto:
    nome = ""
    preco = 0.0
    quantidade_estoque = ""
    categoria = ""

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def get_quantidade_estoque(self):
        return self.quantidade_estoque

    def set_quantidade_estoque(self, quantidade_estoque):
        self.quantidade_estoque = quantidade_estoque

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        print(quantidade, self.nome,"adicionados ao estoque")

    def remover_estoque(self, quantidade):
        if self.quantidade_estoque > quantidade:
            self.quantidade_estoque -= quantidade
            print(">",quantidade,"unidades de",self.nome,"removidos do estoque")
        else:
            print(self.nome,"Impossível remover",quantidade,self.nome,": Estoque insuficiente")

    def aplicar_desconto(self, desc):
        self.preco -= self.preco * desc / 100
        print("> Desconto de",desc,"% aplicado ao produto")

    def exibir_dados(self):
        print(self.nome,"|","R$",self.preco,"|",self.quantidade_estoque,"unidades","|",self.categoria)


produto1 = Produto()
produto1.nome = "Pão Doce"
produto1.preco = 9.0
produto1.quantidade_estoque = 40
produto1.categoria = "Pereciveis"
produto1.exibir_dados()
produto1.aplicar_desconto(20)
produto1.remover_estoque(27)
produto1.exibir_dados()
produto1.remover_estoque(15)
produto1.exibir_dados()
print("////////")
produto2 = Produto()
produto2.nome = "Desodorante"
produto2.preco = 14.00
produto2.quantidade_estoque = 150
produto2.categoria = "Higiene"
produto2.exibir_dados()
produto2.aplicar_desconto(15)
produto2.remover_estoque(70)
produto2.exibir_dados()