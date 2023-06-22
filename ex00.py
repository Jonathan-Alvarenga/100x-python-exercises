import random

class JoKenPo:
    def mostrarOpcoes(self):
        print("Suas opções:")
        print("[ 1 ] PEDRA")
        print("[ 2 ] PAPEL")
        print("[ 3 ] TESOURA")

    def entradaJogador(self):
        escolhaPlayer = int(input("Qual é a sua jogada? "))
        escolhaMaquina = random.randint(1, 3)
        return escolhaPlayer, escolhaMaquina

    def calcularVencedor(self):
        escolhaPlayer, escolhaMaquina = self.entradaJogador()
        if escolhaPlayer == escolhaMaquina:
            print("Empate!")
        elif (
            (escolhaPlayer == 1 and escolhaMaquina == 3) or
            (escolhaPlayer == 2 and escolhaMaquina == 1) or
            (escolhaPlayer == 3 and escolhaMaquina == 2)
        ):
            print("Você venceu!")
        else:
            print("Você perdeu!")

        retry = input("Deseja jogar novamente? S/N ")

        self.jogarNovamente(retry)

    def jogarNovamente(self, retry):
        if retry.lower() == "s":
            self.executaJogo()
        else:
            exit()

    def executaJogo(self):
        self.mostrarOpcoes()
        self.calcularVencedor()

jogo = JoKenPo()
jogo.executaJogo()