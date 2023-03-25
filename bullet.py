import pygame

bullet_img = pygame.image.load("assets/images/icons/bullet.png").convert_alpha()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, flip):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.flip = flip
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #self.direction = direction
    
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
        
        




