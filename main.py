# importando as bibliotecas
import pygame
from pygame.locals import *
from sys import exit  # função para fechar a janela

# iniciando o pygame

pygame.init()

# altura e largura da tela

largura = 640
altura = 640

# criando a tela

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SNAKE GAME')

# loop infinito para roda o jogo

while True:
    # loop for vai checar os eventos que vão ocorrer
    for event in pygame.event.get():
        # função para fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
    # atualiza a tela do jogo a cada interação do loop principal
    pygame.display.update()
