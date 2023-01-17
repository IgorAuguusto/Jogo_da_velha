# Jogo da Velha
Este é um jogo simples da velha implementado em Python. O jogo é jogado no console e consiste em um tabuleiro 3x3 onde o jogador marca sua jogada com "O" e o computador marca com "X".

## Como jogar
Para jogar, execute o arquivo _**jogo_da_velha.py**_ em um interpretador Python. O tabuleiro inicial será exibido e o jogador será solicitado a entrar com o número da sua jogada. O jogador deve escolher uma posição válida no tabuleiro (números de 1 a 9) e pressionar Enter. O tabuleiro será atualizado com a jogada do jogador e, em seguida, será a vez do computador jogar. O jogo continua até que alguém ganhe ou ocorra um empate.

## Funcionalidades
* O jogo contém uma classe jogo_da_velha que inicializa o tabuleiro e contém os métodos para exibir o tabuleiro atual, aceitar jogadas do usuário, verificar vitórias e empates.
* O tabuleiro é representado como uma lista de listas em Python, onde cada elemento da lista representa uma posição no tabuleiro (1 a 9)
* O jogador é solicitado a entrar com sua jogada e o tabuleiro é atualizado com a jogada do jogador.
* O computador tem a jogada aleatória e o tabuleiro é atualizado com a jogada do computador
* O jogo verifica se houve vitória ou empate a cada jogada.
* O jogo não tem a opção de reiniciar ou sair
## Limitacoes
* O jogo só termina quando há vitória ou empate, mas não há nenhuma forma de sair do jogo ou reiniciar uma nova partida.
* O jogo não possui a opção de escolher com quem jogar (computador ou player)
## Melhorias Futuras
* Adicionar a opção de reiniciar ou sair do jogo.
* Adicionar a opção de escolher com quem jogar.
* Adicionar uma interface gráfica para o jogo.
#
Este projeto é um exemplo básico de jogo da velha e pode ser usado como base para desenvolvimento de jogos mais complexos. Sinta-se à vontade para fazer melhorias no código e adicionar novas funcionalid
