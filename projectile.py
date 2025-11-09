import pygame


#definir la classe qui va gerer le projectile de note joeur
class projectile(pygame.sprite.Sprite):
    #definir le constructeur de cette classe
    def __init__(self,player):
        super().__init__()
        self.player = player
        self.velocity=2
        self.image=pygame.image.load("PygameAssets-main/projectile.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.x=player.rect.x+120
        self.rect.y=player.rect.y+80
        self.origin_image=self.image
        self.angle=0

    def rotate(self):
        #tourner le projectile
        self.angle+=5
        self.image=pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect=self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):
        self.rect.x+=self.velocity
        self.rotate()
        # verifier si prjectile entre en collision avec un monster
        for monster in  self.player.game.check_collisions(self,self.player.game.all_monsters):
            #supprimer projectille
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

        #veriier si notre projectile n'est plus recent sur l'ecran
        if self.rect.x>1080:
            self.remove()






