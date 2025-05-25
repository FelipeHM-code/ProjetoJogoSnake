import pygame
import random

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [pygame.image.load(f'images/moeda{i}.PNG') for i in range(1, 6)]
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 500)

    def update(self):
        self.atual += 0.40
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = pygame.transform.scale(self.sprites[int(self.atual)], (13, 16))

    def reposicionar(self):
        self.rect.x = random.randint(40, 600)
        self.rect.y = random.randint(50, 430)
