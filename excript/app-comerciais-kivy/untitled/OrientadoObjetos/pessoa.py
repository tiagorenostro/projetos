class Porta:
    def __init__(self, cor):
        self.cor = cor


class Casa:
    def __init__(self, porta, area):
        self.porta = porta
        self.area = area
        self.descricao = 'Casa'


class Apartamento(Casa):
    def __init__(self, porta):
        self.porta = porta
        self.area = 50
        self.descricao = 'Apartamento'


class Pessoa():
    def __init__(self, nome, moradia):
        self.nome = nome
        self.moradia = moradia

    def get_moradia(self):
        return 'Meu nome é {}, tenho um {} de {}m2 com a porta {}'.format(self.nome, self.moradia.descricao, self.moradia.area, self.moradia.porta.cor)


p1 = Porta('Cinza')
c1 = Casa(p1, 100)
pessoa1 = Pessoa('Tiago', c1)

p2 = Porta('Marrom')
ap1 = Apartamento(p2)
pessoa2 = Pessoa('Maria', ap1)
print(pessoa1.get_moradia())
print(pessoa2.get_moradia())