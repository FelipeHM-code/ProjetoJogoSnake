import pygame

largura = 840
altura = 640
tamanho_bloco = 20
velocidade = 10
FPS = 30

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Primeiro Jogo')

fonte = pygame.font.SysFont('arial', 40, True, True)
