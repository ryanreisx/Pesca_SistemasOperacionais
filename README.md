# Pesca_SistemasOperacionais
Jogo de pesca com aplicação de Semáforos e Threads para a disciplina de Sistemas Operacionais da UFBA.


Manual do Jogo de Pesca

Bem-vindo ao Jogo de Pesca! Este jogo é para dois jogadores, onde cada jogador tenta capturar peixes em um mapa 3x3. O primeiro jogador a atingir 3 pontos vence o jogo.

Regras do Jogo:
  -O mapa do jogo é criado aleatoriamente com 0s e 1s, onde 1 representa um peixe e 0 representa uma posição vazia.
  -Os jogadores alternam entre si para escolher uma coordenada no mapa para jogar sua isca.
  -Se houver um peixe na coordenada escolhida, o jogador deve esperar 3 rodadas para puxá-lo e ganhar um ponto.
  -Se não houver um peixe na coordenada escolhida, o jogador não ganha pontos.
  -O primeiro jogador a atingir 3 pontos vence o jogo.
Como Jogar:
  -Execute o código do jogo em um ambiente de desenvolvimento Python.
  -O jogo começará com uma mensagem de boas-vindas e o mapa do jogo será exibido.
  -O jogador 1 começa escolhendo uma coordenada no mapa para jogar sua isca. Insira a coordenada X (0-2) e a coordenada Y (0-2) quando solicitado.
  -Se houver um peixe na coordenada escolhida, o jogador 1 deve esperar 3 rodadas para puxá-lo e ganhar um ponto. Se não houver um peixe na coordenada escolhida, o jogador não ganha pontos.
  -O jogador 2 agora escolhe uma coordenada no mapa para jogar sua isca. Insira a coordenada X (0-2) e a coordenada Y (0-2) quando solicitado.
  -Se houver um peixe na coordenada escolhida, o jogador 2 deve esperar 3 rodadas para puxá-lo e ganhar um ponto. Se não houver um peixe na coordenada escolhida, o jogador não ganha pontos.
  -O jogo continua alternando entre os jogadores até que um dos jogadores atinja 3 pontos e vença o jogo.
  -Observação: Se uma coordenada já foi ocupada por um jogador, o próximo jogador deve escolher uma coordenada diferente.
