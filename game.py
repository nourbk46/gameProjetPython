import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import Soundmanager


#creer seconde class game
class Game:
    def __init__(self):
        #definir si notre jeu a commancer
        self.is_playing=False
        # groupe de joueurs
        self.all_players=pygame.sprite.Group()
        self.player=Player(self)
        self.all_players.add(self.player)
        #generer event
        self.comet_event=CometFallEvent(self)
        #groupe de monsters
        self.all_monsters=pygame.sprite.Group()
        #gerer le son
        self.sound_manager=Soundmanager()
        #metre le score a 0
        self.font = pygame.font.Font("PygameAssets-main/PottaOne.ttf", 20)
        self.score=0
        # touches pressées
        self.pressed={
        }


    def start(self):
        self.is_playing=True
        # apparaitre des monstres
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self,points=10):
        self.score+=points


    def game_over(self):
        #remettre le jeu a neuf
        self.all_monsters=pygame.sprite.Group()
        self.comet_event.all_comets=pygame.sprite.Group()
        self.player.health=self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing=False
        self.score=0
        #jouer le son
        self.sound_manager.play('game_over')


    def update(self,screen):
        #afficher le score dans l'ecran

        score_text=self.font.render(f"Score: {self.score}",1,(0,0,0))
        screen.blit(score_text,(20,20))

        # appliquer image joeur
        screen.blit(self.player.image, self.player.rect)
        # actualiser la barre de vie de joeur
        self.player.update_health_bar(screen)

        #actualiser barre event jeu
        self.comet_event.update_bar(screen)

        #actualiser l'animation  joeur
        self.player.update_animation()


        # recuperer les projectiles des joeurs
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monsters des joeurs
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()


        #recuperer les comet de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monsters
        self.all_monsters.draw(screen)

        #appliquer ensemble des images de  mon groupe de comets
        self.comet_event.all_comets.draw(screen)

        # verifier si joeur veut gauche ou droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        print(self.player.rect.x)


    def check_collisions(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)



    def spawn_monster(self,monster_class_name):

        self.all_monsters.add(monster_class_name.__call__(self))


