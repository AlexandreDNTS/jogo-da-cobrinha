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

velocidade = 10
x_controle = velocidade
y_controle = 0
# criando a tela

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SNAKE GAME')

# relogio(frames por segundo)
relogio = pygame.time.Clock()
# pontuação
pontos = 0
# funções

lista_cobra = []
comprimento_inicial = 2


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = [x,y]
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


morreu = False


def reinicia_jogo():
    global morreu, pontos, comprimento_inicial, y_controle, x_controle, y_maca, x_maca, y_snake, x_snake, lista_cabeca, lista_cobra
    morreu = False
    pontos = 0
    comprimento_inicial = 2
    y_maca = altura//2
    x_maca = 580
    y_snake = altura//2
    x_snake = largura//2
    lista_cabeca = []
    lista_cobra = []
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
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    x_snake = x_snake + x_controle
    y_snake = y_snake + y_controle
    # criando a maçã e a cobra
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 20, 20))
    # condições de colisões
    if snake.colliderect(maca):
        pontos += 1
        x_maca = randint(10, 580)
        y_maca = randint(10, 580)
        comprimento_inicial += 1
    # crescimento da cobra

    lista_cabeca = []
    lista_cabeca.append(x_snake)
    lista_cabeca.append(y_snake)
    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        msg2 = 'Game over! pressione a tecla R para jogar novamente'
        textoFormatado2 = fonte2.render(msg2, True, (0, 0, 0))
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reinicia_jogo()
            tela.blit(textoFormatado2, (55, altura//2))
            pygame.display.update()
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    # atualiza a tela do jogo a cada interação do loop principal
    tela.blit(textoFormatado, (450, 40))
    pygame.display.update()
