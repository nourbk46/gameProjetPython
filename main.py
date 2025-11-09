import pygame
import math
from game import Game
pygame.init()
#gen9erer fenetre
pygame.display.set_caption("comet full game")
screen=pygame.display.set_mode((1000,700))

background=pygame.image.load('PygameAssets-main/bg.jpg')

#importer notre banniere
banner=pygame.image.load('PygameAssets-main/banner.png')
banner=pygame.transform.scale(banner,(500,500))
banner_rect=banner.get_rect()
banner_rect.x=math.ceil(screen.get_width()/4)

#importer bouton pour lancer la partie
play_button=pygame.image.load('PygameAssets-main/button.png')
play_button=pygame.transform.scale(play_button,(400,150))
play_button_rect=play_button.get_rect()
play_button_rect.x=math.ceil(screen.get_width()/3.33)
play_button_rect.y=math.ceil(screen.get_height()/1.91)

#charger notre joeur
game=Game()
running=True

while running:
    #appliquer background
    screen.blit(background,(0,-200))
    #verifier si notre jeu a commencer ou non
    if game.is_playing:
        #declencher les instructions de la partie
        game.update(screen)
    #verifier si notre jeu n'a pas commencer
    else:
        #ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner,banner_rect)


    #mettre a jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("fermuture de jeu")
        #detecter si joeur lanche clavier
        elif event.type==pygame.KEYDOWN:
            game.pressed[event.key]=True

            #detecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key==pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type==pygame.KEYUP:
            game.pressed[event.key]=False

        elif event.type==pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()


