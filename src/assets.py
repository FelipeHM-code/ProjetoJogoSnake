import pygame

pygame.mixer.init()

pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('sons/Musica_de_fundo.mp3')
pygame.mixer.music.play(-1)

barulho_colosao = pygame.mixer.Sound('sons/smw_dragon_coin.wav')
barulho_colosao.set_volume(1)

imagem_fundo = pygame.image.load('images/fajrbackground.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (840, 640))
