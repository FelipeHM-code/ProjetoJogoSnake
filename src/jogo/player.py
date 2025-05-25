from config import largura, altura, tamanho_bloco
import pygame

class Player:
    def __init__(self):
        self.x = largura // 2
        self.y = altura // 2
        self.velocidade = 10
        self.x_controle = 20
        self.y_controle = 0

        self.image = pygame.Surface((tamanho_bloco, tamanho_bloco))
        self.image.fill((255, 0, 0))  # Define a cor do jogador
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.lista_cobra = [[self.x - (i * tamanho_bloco), self.y] for i in range(5)]
    
    def atualizar_movimento(self, tecla):
        if tecla == "LEFT" and self.x_controle != self.velocidade:
            self.x_controle = -self.velocidade
            self.y_controle = 0
        elif tecla == "RIGHT" and self.x_controle != -self.velocidade:
            self.x_controle = self.velocidade
            self.y_controle = 0
        elif tecla == "UP" and self.y_controle != self.velocidade:
            self.y_controle = -self.velocidade
            self.x_controle = 0
        elif tecla == "DOWN" and self.y_controle != -self.velocidade:
            self.y_controle = self.velocidade
            self.x_controle = 0

    def movimentar(self):
        self.x += self.x_controle
        self.y += self.y_controle
        self.rect.topleft = (self.x, self.y)

        if self.x > largura:
            self.x = 0
        elif self.x < 0:
            self.x = largura

        if self.y > altura:
            self.y = 0
        elif self.y < 0:
            self.y = altura
