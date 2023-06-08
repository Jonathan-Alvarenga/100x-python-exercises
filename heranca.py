class Cachorro():
    def __init__(self, nome, porte, raca, cor_pelo):
        self.nome = nome
        self.porte = porte
        self.raca = raca
        self.cor_pelo = cor_pelo

    def exibir_informacoes(self):
        print(f'Nome do cachorro é {self.nome}')
        print(f'O porte do cachorro é {self.porte}')
        print(f'A raça do cachorro é {self.raca}')
        print(f'E a cor do pelo do cachorro é {self.cor_pelo}\n')


rex = Cachorro('Rex', 'médio', 'Poodle', 'Branco')
alice = Cachorro(nome='Alice', raca='Pitbull', porte='Grande', cor_pelo='Preta')
café = Cachorro('Café', 'pequeno', 'Caramelo', 'Preto')
# ----------------------
rex.exibir_informacoes()
alice.exibir_informacoes()
café.exibir_informacoes()
