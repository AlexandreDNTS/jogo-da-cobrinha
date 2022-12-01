# importando as bibliotecas
import pygame
from pygame.locals import *
from sys import exit  # função para fechar a janela
from random import randint

# iniciando o pygame

pygame.init()

# altura e largura da tela

largura = 640
altura = 640

# texto
fonte = pygame.font.SysFont('arial', 40, False, True,)
# posição da maca e da coobra
y_maca = altura//2
x_maca = 580

y_snake = altura//2
x_snake = largura//2
# criando a tela

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SNAKE GAME')

# relogio(frames por segundo)
relogio = pygame.time.Clock()
# pontuação
pontos = 0
# loop infinito para roda o jogo

while True:
    # frames
    relogio.tick(30)
    # cor da tela
    tela.fill((0, 120, 0))
    # texto
    msg = f'pontos: {pontos}'
    textoFormatado = fonte.render(msg, False, (255, 255, 255))
    # loop for vai checar os eventos que vão ocorrer
    for event in pygame.event.get():
        # função para fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
    # movimentação
    if pygame.key.get_pressed()[K_a]:
        x_snake = x_snake-15
    if pygame.key.get_pressed()[K_d]:
        x_snake = x_snake+15
    if pygame.key.get_pressed()[K_w]:
        y_snake = y_snake-15
    if pygame.key.get_pressed()[K_s]:
        y_snake = y_snake+15
    # criando a maçã e a cobra
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 25, 25))
    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 25, 25))
    # condições de colisões
    if snake.colliderect(maca):
        pontos = pontos+1
        x_maca = randint(10, 580)
        y_maca = randint(10, 580)
    # atualiza a tela do jogo a cada interação do loop principal
    tela.blit(textoFormatado, (450, 40))
    pygame.display.update()
