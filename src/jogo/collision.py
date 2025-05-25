from assets import barulho_colosao


def verificar_colisao(player, inimigo, pontos):
    if player.rect.colliderect(inimigo.rect):
        inimigo.reposicionar()
        pontos += 1
        barulho_colosao.play()
        
        # Aumenta o tamanho da cobra
        player.lista_cobra.append([player.x, player.y])
        
        # Aumenta a velocidade
        player.velocidade += 0.2
    
    return pontos
