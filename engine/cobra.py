import pygame
from config import *

class cobra:    #Configurando a cobra
    def __init__(self):
        self.corpo = []
        self.direcao = velocidade
        self.comprimento = compri_inicial
        self.x = largura //2
        self.y = altura //2

    def mover(self):
        self.x += self.direcao[0]
        self.y += self.direcao[1]

        #Logica para mover e colidir

    def desenhar(self, tela):
        for parte in self.corpo:
            pygame.draw.rect(tela,(255,0,0),(*parte, Tamanho_bloco, Tamanho_bloco))
    