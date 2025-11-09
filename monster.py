import pygame
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game=game
        self.health=100
        self.max_health=100
        self.attack=5
        self.image=pygame.image.load("PygameAssets-main/mummy.png")
        self.rect=self.image.get_rect()
        self.rect.x=900+random.randint(0,300)
        self.rect.y=540
        self.velocity=random.randint(1,2)

    def damage(self,amount):
        #infliger les degats
        self.health-=amount

        #verifier nombrs de point de vie inf ou egal a 0
        if self.health<=0:
            self.rect.x=1000+random.randint(0,300)
            self.velocity=random.randint(1,2)
            self.health=self.max_health



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