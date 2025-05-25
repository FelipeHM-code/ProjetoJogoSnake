import pygame
from config import tela, fonte
from assets import imagem_fundo
from jogo.player import Player
from jogo.enemy import Inimigo
from jogo.collision import verificar_colisao

pygame.init()
relogio = pygame.time.Clock()

player = Player()
inimigo = Inimigo()
sprites = pygame.sprite.Group()
sprites.add(inimigo)

pontos = 0
morreu = False

while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))
    tela.blit(imagem_fundo, (0, 0))

    mensagem = f"Pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, False, (0, 0, 0))
    tela.blit(texto_formatado, (560, 30))

    tela.blit(player.image, player.rect)


    sprites.draw(tela)
    sprites.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                player.atualizar_movimento("LEFT")
            elif evento.key == pygame.K_d:
                player.atualizar_movimento("RIGHT")
            elif evento.key == pygame.K_w:
                player.atualizar_movimento("UP")
            elif evento.key == pygame.K_s:
                player.atualizar_movimento("DOWN")

    player.movimentar()
    pontos = verificar_colisao(player, inimigo, pontos)
    pygame.display.flip()
