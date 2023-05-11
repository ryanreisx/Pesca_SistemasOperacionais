# Importando bibliotecas necessárias
import threading
import numpy as np


print("------------------------------------------------------------------------------")
print("Bem vindo ao jogo de pesca! Escolha a coordenada onde você quer jogar sua isca!")
print("------------------------------------------------------------------------------")

# Criando o mapa do jogo com 0s e 1s aleatoriamente
mapa = np.random.choice([0, 1], size=(3, 3))
print("")

# Inicializando variáveis para armazenar informações do jogo
coordenadas_ocupadas = {}
coordenadas_semaforo = []
for i in range(3):
  for j in range(3):
    coordenadas_semaforo.append(threading.Semaphore())

pontuação = [0, 0]
jogador_atual = 0
rounds_espera = [0, 0]

# Função para capturar peixe
def capturar_peixe(x, y, jogador):
  """Captura um peixe na coordenada (x, y) pelo jogador.
    Args:
        x (int): Coordenada X.
        y (int): Coordenada Y.
        jogador (int): Identificador do jogador."""
  
  global mapa, pontuação, coordenadas_ocupadas, coordenadas_semaforo, rounds_espera

  semaforo = coordenadas_semaforo[x * 3 + y]
  semaforo.acquire()

  # Verifica se a coordenada já foi ocupada
  if (x, y) in coordenadas_ocupadas:
    print(f"Jogador {jogador + 1}, essa coordenada já está ocupada.")
  # Verifica se há um peixe na coordenada
  elif mapa[x][y] == 1:
    mapa[x][y] = 0
    rounds_espera[jogador] = 3
    coordenadas_ocupadas[(x, y)] = jogador
    print(f"Jogador {jogador + 1} encontrou um peixe! Esperando 3 rounds para poder puxá-lo...")
  # Caso não haja peixe na coordenada
  else:
    print(f"Jogador {jogador + 1} não encontrou um peixe!")

  semaforo.release()

# Função para jogar
def jogar(jogador):
  """Joga o jogo de pesca com o jogador especificado.
    Args: 
        jogador (int): Identificador do jogador."""
        
  global jogador_atual, rounds_espera

  # Loop enquanto jogador não atingir pontuação 3
  while pontuação[jogador] < 3:
    if jogador_atual == jogador:
      # Se jogador está esperando para puxar um peixe
      if rounds_espera[jogador] > 0:
        print(f"Jogador {jogador + 1} aguardando {rounds_espera[jogador]} round(s).")
        rounds_espera[jogador] -= 1
        if rounds_espera[jogador] == 0:
          pontuação[jogador] += 1
          print(f"Jogador {jogador + 1} recebeu 1 ponto! Pontuação: {pontuação[jogador]}")
          if pontuação[jogador] == 3:
            print(f"Jogador {jogador+1} venceu!")
            break
      # Se jogador está escolhendo coordenada para jogar isca
      else:
        x = int(input(f"Jogador {jogador + 1}, insira a coordenada X (0-2): "))
        y = int(input(f"Jogador {jogador + 1}, insira a coordenada Y (0-2): "))
        capturar_peixe(x, y, jogador)

      # Alterna entre os jogadores
      jogador_atual = (jogador_atual + 1) % 2

# Inicializando e iniciando as threads dos jogadores
t1 = threading.Thread(target=jogar, args=(0, ))
t2 = threading.Thread(target=jogar, args=(1, ))

t1.start()
t2.start()

t1.join()
t2.join()
