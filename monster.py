import pygame
import random
import animation

class Monster(animation.AnimateSprite):
    def __init__(self,game,name,size,offset=0):
        super().__init__(name,size)
        self.game=game
        self.health=100
        self.max_health=100
        self.attack=0.3
        self.rect=self.image.get_rect()
        self.rect.x=900+random.randint(0,300)
        self.rect.y=540-offset
        self.velocity=random.randint(1,1)
        self.loot_amount=10
        self.start_animation()

    def set_speed(self,speed):
        self.default_speed=speed
        self.velocity=random.randint(1,speed)

    def set_loot_amount(self,amount):
        self.loot_amount=amount


    def damage(self,amount):
        #infliger les degats
        self.health-=amount

        #verifier nombrs de point de vie inf ou egal a 0
        if self.health<=0:
            self.rect.x=1000+random.randint(0,300)
            self.velocity=random.randint(1,self.default_speed)
            self.health=self.max_health
            #ajouter le nb de points
            self.game.add_score(self.loot_amount)

            #si la barre d'event  est chargé a son max
            if self.game.comet_event.is_full_loaded():
                #retirer de jeu
                self.game.all_monsters.remove(self)

                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self,surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface,(111,210,64),[self.rect.x+10,self.rect.y-20,self.health,5])


    def forward(self):
        #le deplacement fait que si n'a pas de collisions avc le joeur
        if not self.game.check_collisions(self,self.game.all_players):
            self.rect.x-=self.velocity
        #si le monster est en collision avec le joeur
        else:
            #infliger les degats
            self.game.player.damage(self.attack)

#def classe pour mummy
class Mummy(Monster):
    def __init__(self,game):
        super().__init__(game,"mummy",(130,130))
        self.set_speed(3)
        self.set_loot_amount(20)

#def classe pour l'alian
class Alien(Monster):
    def __init__(self,game):
        super().__init__(game,"alien",(300,300),150)
        self.health=250
        self.max_health=250
        self.attack=0.8
        self.set_speed(1)
        self.set_loot_amount(80)
