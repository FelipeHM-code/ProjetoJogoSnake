import pygame
from pygame.locals import *
from sys import exit   #para importar de sistema o comando exit para criar a saida da tela
from random import randint
import random

pygame.init()  #para iniciar o pygame



pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('Musica_de_fundo.mp3')
pygame.mixer.music.play(-1)

barulho_colosao = pygame.mixer.Sound('smw_dragon_coin.wav')
barulho_colosao.set_volume(1)
largura =840
altura = 640
tela=pygame.display.set_mode((largura, altura))
imagem_fundo = pygame.image.load('moedas/fajrbackground.png').convert()
imgem_fundo = pygame.transform.scale(imagem_fundo,(largura,altura))
x_persona = largura/2 #diz em qual lugar o boneco nasce
y_persona = altura/2

velocidade = 10
x_controle = 20
y_controle = 0

lista_cobra = []
compri_inicial = 5

fonte = pygame.font.SysFont('arial',40,True,True)
pontos = 0
#tela=pygame.display.set_mode((largura, altura))#variavel tela com o comando para criar uma janela, chamando o ste mode com as conf de largura e
#altura
morreu = False



relogio = pygame.time.Clock()#cria um objeto que ajuda a controlar a taxa de frame do jogo, quanto mais frame mais rapido e quanto menos mais
# lento
def aumenta_cobra (lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(255,0,0), (XeY[0],XeY[1],20,20))

def reiniciar_jogo():
   global pontos, compri_inicial, x_persona, y_persona,lista_cabeca,lista_cobra, morreu,velocidade
   pontos = 0
   velocidade = 10
   compri_inicial = 5
   x_persona = largura/2
   y_persona = altura/2
   lista_cobra = []
   lista_cabeca = []
   morreu = False
 

pygame.display.set_caption('Primeiro Jogo')#serve para alterar o nome da janela na parte de cima

''''class Cabeca_cobra(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load('moedas/cobracabeca.PNG').convert_alpha()
      self.image = pygame.transform.scale(self.image, (20,20))
      self.rect = self.image.get_rect()
      self.rect.topleft = (largura//2,altura//2)
    
   def update_pos(self,x , y):
      self.rect.x = x
      self.rect.y = y'''


class Inimigo(pygame.sprite.Sprite):
   def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.sprites = []
    self.sprites.append(pygame.image.load('moedas/moeda1.PNG'))
    self.sprites.append(pygame.image.load('moedas/moeda2.PNG'))
    self.sprites.append(pygame.image.load('moedas/moeda3.PNG'))
    self.sprites.append(pygame.image.load('moedas/moeda4.PNG'))
    self.sprites.append(pygame.image.load('moedas/moeda5.PNG'))
    self.atual = 0
    self.image = self.sprites[self.atual]
    self.rect = self.image.get_rect()
    self.rect.topleft = 400, 500
    
   def update(self):
      self.atual = self.atual + 0.40
      if self.atual >= len(self.sprites):
          self.atual = 0
      self.image = self.sprites[int(self.atual)]
      self.image = pygame.transform.scale(self.image, (13*1,16*1))
    
   def reposicao(self):
     self.rect.x = random.randint(40,600)
     self.rect.y = random.randint(50,430)


todas_as_sprites = pygame.sprite.Group()
inimigo = Inimigo()
todas_as_sprites.add(inimigo)
#cabeca_cobra = Cabeca_cobra()
#todas_as_sprites.add(cabeca_cobra)

while True:
    relogio.tick(30)#pega a variavel RELOGIO e fala para ela a quantidade de frames por segundo
    tela.fill((255,255,255))
    mensagem = f"Pontos: {pontos}"
    texto_format = fonte.render(mensagem, False, (0,0,0))
    tela.blit(imagem_fundo,(0,0))

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            exit()
            
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: 
                if x_controle == velocidade:
                    pass
                else:
                 x_controle = -velocidade
                 y_controle = 0
            if event.key == pygame.K_d:
                if x_controle == - velocidade:
                    pass
                else:
                 x_controle = velocidade
                 y_controle = 0
            if event.key == pygame.K_w:
                if y_controle == velocidade:
                    pass
                else:
                 y_controle = - velocidade
                 x_controle = 0
            if event.key == pygame.K_s:
                if y_controle == -velocidade:
                    pass
                else:
                 y_controle = velocidade
                 x_controle = 0

    x_persona  = x_persona + x_controle
    y_persona = y_persona + y_controle          
 
    ret_persona = pygame.draw.rect(tela, (255, 0, 0), (x_persona, y_persona, 20,20))                                  #serve para criar um quadrado na tela, persona é quadrado, tela é variavel a cima
    ret_objeto =  inimigo                                   # o (255, 0, 0) é a coloracão rgb, o x e y é a variavel do tamanho da tela, o 40, 50 é o ponto cartesiano para criar o quadrado, 40 o primeiro
                                                                                                      #pixel da ponta da esquerda em cima do quadrado e o 50 é o ponto da direita em cima
    if ret_persona.colliderect(inimigo.rect):
       inimigo.reposicao()
       pontos = pontos+1
       barulho_colosao.play()
       compri_inicial += 1
       velocidade += 0.2

    lista_cabeca = []
    lista_cabeca.append(x_persona)
    lista_cabeca.append(y_persona)
    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca) > 1:
       fonte2 = pygame.font.SysFont('arial',40,True, True)
       mensagem2 = "Pressione a tecla (R) para Reiniciar o jogo"
       text_format = fonte2.render(mensagem2,True, (0,0,0))
       ret_texto = text_format.get_rect()

       morreu = True 
       while morreu:
        tela.fill((255,255,255)) 
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
               if event.key == K_r:
                  reiniciar_jogo()
        ret_texto.center = (largura//2,altura//2)
        tela.blit(text_format,ret_texto)
        pygame.display.flip()
    if x_persona > largura :
       x_persona = 0
    if x_persona < 0:
       x_persona = largura
    if y_persona < 0:
       y_persona = altura
    if y_persona > altura:
       y_persona = 0


    if len(lista_cobra) > compri_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    tela.blit(texto_format,(560,30))
    pygame.display.flip()
