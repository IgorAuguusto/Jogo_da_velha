#!/usr/bin/env python3
from mimetypes import init
from random import randrange


class jogo_da_velha():
    def __init__(self):
        self.tabuleiro = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

    def status_placa(self):
        #  O metodo contendo o status atual da placa
        # e imprime no console.
        print('''
                +-------+-------+-------+
                |       |       |       |
                |   {}   |   {}   |   {}   |
                |       |       |       |
                +-------+-------+-------+
                |       |       |       |
                |   {}   |   {}   |   {}   |
                |       |       |       |
                +-------+-------+-------+
                |       |       |       |
                |   {}   |   {}   |   {}   |
                |       |       |       |
                +-------+-------+-------+'''.format(self.tabuleiro[0][0], self.tabuleiro[0][1], self.tabuleiro[0][2],
                                                    self.tabuleiro[1][0], self.tabuleiro[1][1], self.tabuleiro[1][2],
                                                    self.tabuleiro[2][0], self.tabuleiro[2][1], self.tabuleiro[2][2]))

    def entre_movimento(self):
        # O metodo aceita o status atual da placa, pergunta ao usuário sobre sua jogada,
        # verifica a entrada e atualiza a placa de acordo com a decisão do usuário.
        jogada = int(input("Entre com o número da sua jogada: "))
        verifica = True
        if jogada > 0 and jogada < 10:
            for l in range(len(self.tabuleiro)):
                for c in range(len(self.tabuleiro[0])):
                    if jogada == self.tabuleiro[l][c]:
                        self.tabuleiro[l][c] = 'O'
                        verifica = True
                        return self.status_placa()

            if verifica:
                print("\nJogada Inválida, posição ocupada!")
                print("Tente novamente\n")
                self.entre_movimento()
        else:
            print("Jogada Inválida !")
            print("Tente novamente")
            self.entre_movimento()

    def lista_de_campos_livres(self):
        # O metodo navega no tabuleiro e constrói uma lista de todos os quadrados livres;
        # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
        # se a tupla estiver vazia, ocorreu um empate
        vazio = 0
        posicao_vazia = ()
        for l in range(len(self.tabuleiro)):
            for c in range(len(self.tabuleiro[0])):
                vazio += 1
                if self.tabuleiro[l][c] == vazio:
                    posicao_vazia += (l, c,)
        if posicao_vazia == ():
            print("EMPATE")
            return True
        else:
            del posicao_vazia

    def vitoria_para(self, sinal):
        # O metodo analisa o estado da placa para verificar se
        # o jogador usando 'O's ou 'X's ganhou o jogo
        # verificando se ganhou pela linha
        for l in range(len(self.tabuleiro)):
            x = self.tabuleiro[l][0]
            cont = 0
            for c in range(len(self.tabuleiro[0])):
                if x == self.tabuleiro[l][c]:
                    cont += 1
                    if cont == 3 and sinal == 'O':
                        print("Você venceu !! :) ")
                        return True
                    if cont == 3 and sinal == 'X':
                        print("Você Perdeu :( ")
                        return True

        # Verificando se ganhou pela coluna
        for c in range(len(self.tabuleiro[0])):
            x = self.tabuleiro[0][c]
            cont = 0
            for l in range(len(self.tabuleiro)):
                if x == self.tabuleiro[l][c]:
                    cont += 1
                    if cont == 3 and sinal == 'O':
                        print("Você venceu !! :) ")
                        return True
                    if cont == 3 and sinal == 'X':
                        print("Você Perdeu :( ")
                        return True
        # Verifica se ganhou pela Diagonal
        cont = 0
        for d in range(len(self.tabuleiro)):
            if self.tabuleiro[0][0] == self.tabuleiro[d][d]:
                cont += 1
                if cont == 3:
                    print("Você Perdeu :(")
                    return True
        # Verifica se ganhou pela diagonal
        cont = 0
        c = 2
        for d in range(len(self.tabuleiro)):
            if self.tabuleiro[0][2] == self.tabuleiro[d][c]:
                cont += 1
                c -= 1
                if cont == 3:
                    print("Você Perdeu :(")
                    return True

    def pc_movimento(self):
        # O metodo desenha o movimento do computador e atualiza o tabuleiro
        jogada_computador = randrange(1, 10)
        verifica = True
        for l in range(len(self.tabuleiro)):
            for c in range(len(self.tabuleiro[0])):
                if jogada_computador == self.tabuleiro[l][c]:
                    self.tabuleiro[l][c] = 'X'
                    verifica = True
                    return self.status_placa()

        if verifica:
            self.pc_movimento()


def main():
    jogo = jogo_da_velha()

    jogo.status_placa()
    while True:
        jogo.entre_movimento()
        if jogo.vitoria_para('O') == True:
            break
        elif jogo.lista_de_campos_livres() == True:
            break
        jogo.pc_movimento()
        if jogo.vitoria_para('X') == True:
            break
        elif jogo.lista_de_campos_livres() == True:
            break


if __name__ == '__main__':
    main()
