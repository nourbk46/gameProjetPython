import pygame
import random

import comet_event


#crrer  classe pour gerer comete
class Comet(pygame.sprite.Sprite):
    def __init__(self,comet_event):
        super().__init__()
        self.image=pygame.image.load('PygameAssets-main/comet.png')
        self.rect=self.image.get_rect()
        self.velocity=random.randint(1,2)
        self.rect.x=random.randint(20,800)
        self.rect.y=-random.randint(0,800)
        self.comet_event=comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        #verifier si le nb e comets est de 0
        if len(self.comet_event.all_comets)==0:
            print("l'event est fini")
            #remettre la barre a0
            self.comet_event.reset_percent()
            #apparaitre les 2 premiers monsters
            self.comet_event.game.start()

    def fall(self):
        self.rect.y+=self.velocity
        #ne tombe pas dans le sol
        if self.rect.y>=500:
            print("sol")
            #retirer la boule de feu
            self.remove()

            #s'il nya plus e boule de feu sur le jeu
            if len(self.comet_event.all_comets)==0:
                print("l'event est fini")
                #remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #verifier si la boule e feu touche le joeur
        if self.comet_event.game.check_collisions(
            self,self.comet_event.game.all_players):
            print("joeur touchée")
            #retirer la boule de feu
            self.remove()
            #subir 20 points e degats
            self.comet_event.game.player.damage(20)

