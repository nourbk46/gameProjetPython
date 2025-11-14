import pygame
#classequi va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):
    #def les choses a faire a la creation de l'entité
    def __init__(self,sprite_name,size=(200,200)):
        super().__init__()
        self.size=size
        self.image=pygame.image.load(f'PygameAssets-main/{sprite_name}.png')
        self.image=pygame.transform.scale(self.image,size)
        self.current_image=0 #commence l'anim a l'image 0
        self.images=animations.get(sprite_name)
        self.animation=False

    #def methode pour demarrer l'animation
    def start_animation(self):
        self.animation=True

    #definir une methode pour animer le sprite
    def animate(self, loop=False):
        #verifier si l'animation est active pour cet entite
        if self.animation:
            #passer a limage suivante
            self.current_image+=1
            #verifier si on atteint la fin de l'animation
            if self.current_image>=len(self.images):
                self.current_image=0
                #deactivation de l'animation
                self.animation=False
                #verfier si l'animation nest pas moe boucle
                if loop is False:
                    self.animation=False
            #modefier l'image preceente par a suivante
            self.image=self.images[self.current_image]
            self.image=pygame.transform.scale(self.image,self.size)


#def fonction pour charger les images  d'un sprite
def load_animation_images(sprite_name):
    #charger les 24  images
    images=[]
    #recuperer le chemain de dossier pour ce sprite
    path=f"PygameAssets-main/{sprite_name}/{sprite_name}"
    #boucler sur chaque fichier chaque image dans ce ossier
    for num in range(1,24):
        image_path=path+str(num)+".png"
        images.append(pygame.image.load(image_path))
    #renvoyer le contenu de la liste d'image
    return images

#def dictionnaire qui va contenir les images chargées
animations={
    'mummy':load_animation_images('mummy'),
    'player':load_animation_images('player'),
    'alien':load_animation_images('alien')
}