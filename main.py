# importando as bibliotecas
import pygame
from pygame.locals import *
from sys import exit  # função para fechar a janela

# iniciando o pygame

pygame.init()

# altura e largura da tela

largura = 640
altura = 640

# posição da maca e da coobra
y_maca = altura//2
x_maca = 580

y_snake = altura//2
x_snake = largura//2
# criando a tela

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SNAKE GAME')

# loop infinito para roda o jogo

while True:
    # cor da tela
    tela.fill((0, 120, 0))
    # loop for vai checar os eventos que vão ocorrer
    for event in pygame.event.get():
        # função para fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
    # criando a maçã e a cobra
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 25, 25))
    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 25, 25))
    # atualiza a tela do jogo a cada interação do loop principal
    pygame.display.update()
