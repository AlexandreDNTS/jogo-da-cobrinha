import PySimpleGUI as sg
import pygame
from pygame.locals import *
from sys import exit


def jogo():
    pygame.init()
    # criando a tela
    largura = 640
    altura = 640

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('jogo da cobrinha')

    # posiçõe da maçã e da cobra

    x_maca = largura//2
    y_maca = 580
    # laço principal

    while True:
        for event in pygame.event.get():
            # codição para fechar a tela
            if event.type == QUIT:
                pygame.quit()
                exit()
        # criando a maçã e a cobra
        cobra = pygame.draw.rect(tela, (0, 255, 0), (100, 300, 25, 25))
        maca = pygame.draw.rect(tela, (255, 0, 0), (y_maca, x_maca, 25, 25))

        pygame.display.update()


def tela_inicial():
    layout = [
        [sg.Text('\n\t\tJOGO DA COBRINHA \t\t')],
        [sg.Button('Iniciar')]
    ]
    return sg.Window('jogo da cobrinha', layout=layout, finalize=True)


telainicial = tela_inicial()
while True:
    window, eventos, valores = sg.read_all_windows()
    if window == telainicial and eventos == sg.WIN_CLOSED:
        break
    if window == telainicial and eventos == 'Iniciar':
        jogo()
