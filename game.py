import pygame
from player import Player
from monster import Monster

#creer seconde class game
class Game:
    def __init__(self):
        #definir si notre jeu a commancer
        self.is_playing=False
        # groupe de joueurs
        self.all_players=pygame.sprite.Group()
        self.player=Player(self)
        self.all_players.add(self.player)
        #groupe de monsters
        self.all_monsters=pygame.sprite.Group()
        # touches pressées
        self.pressed={
        }


    def start(self):
        self.is_playing=True
        # apparaitre des monstres
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        #remettre le jeu a neuf
        self.all_monsters=pygame.sprite.Group()
        self.player.health=self.player.max_health
        self.is_playing=False


    def update(self,screen):

        # appliquer image joeur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie de joeur
        self.player.update_health_bar(screen)

        # recuperer les projectiles des joeurs
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monsters des joeurs
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monsters
        self.all_monsters.draw(screen)

        # verifier si joeur veut gauche ou droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        print(self.player.rect.x)


    def check_collisions(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)



    def spawn_monster(self):
        monster=Monster(self)
        self.all_monsters.add(monster)


