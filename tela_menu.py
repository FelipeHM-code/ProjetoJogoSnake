import pygame
from sys import exit

def exibir_menu(tela, largura, altura):
    pygame.mixer.music.load('sons/menu.wav')  # Música de menu (opcional)
    pygame.mixer.music.play(-1)

    fonte = pygame.font.SysFont('arial', 50, True)
    rodando = True
    while rodando:
        tela.fill((0, 0, 0))
        titulo = fonte.render('🐍 JOGO DA COBRINHA 🐍', True, (0, 255, 0))
        iniciar = fonte.render('Pressione ENTER para Jogar', True, (255, 255, 255))
        sair = fonte.render('Pressione ESC para Sair', True, (255, 0, 0))

        tela.blit(titulo, (largura//2 - titulo.get_width()//2, 150))
        tela.blit(iniciar, (largura//2 - iniciar.get_width()//2, 250))
        tela.blit(sair, (largura//2 - sair.get_width()//2, 320))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rodando = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
