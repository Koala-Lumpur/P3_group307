import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('WHat is thiis')

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('stock.jpg', [0, 0])
wall = Background('wall.jpeg', [100,100])
screen.blit(BackGround.image, BackGround.rect)

while True:
    screen.blit(wall.image, wall.rect)
    pygame.display.update()
