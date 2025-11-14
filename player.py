import pygame
from projectile import projectile
import animation

#creer premiere class


class Player(animation.AnimateSprite):
    def __init__(self,game):
        super().__init__('player')
        self.game=game
        self.health=100
        self.max_health=100
        self.attack=10
        self.velocity=1
        self.all_projectiles=pygame.sprite.Group()
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=500

    def damage(self,amount):
        if self.health-amount > amount:
            self.health-=amount
        else:
            #si le joeur n'ap pas de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()


    def update_health_bar(self,surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 50, self.rect.y +20, self.max_health, 5])
        pygame.draw.rect(surface,(111,210,64),[self.rect.x+50,self.rect.y+20,self.health,5])


    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(projectile(self))
        #demarer l'animation
        self.start_animation()
        #jouer le son
        self.game.sound_manager.play('tir')




    def move_right(self):
        #si le joeur ne pas en collision avec monster
        if not self.game.check_collisions(self,self.game.all_monsters):
            self.rect.x+=self.velocity
    def move_left(self):
        self.rect.x-=self.velocity

