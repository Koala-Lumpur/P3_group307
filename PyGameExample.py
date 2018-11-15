import pygame
import EdgeDetection
import cv2

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BLACK = (0,0,0)
WHITE = (255,255,255)

camera = cv2.VideoCapture(0)

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('WHat is thiis')

#BackGround = Background('stock.jpg', [0, 0])
background = pygame.image.load("stock.jpg").convert()
screen.blit(background, [0,0])

while True:
    ret, frame = camera.read()
    frame = EdgeDetection.main()
    frame = pygame.surfarray.make_surface(frame)
    frame.set_colorkey((0, 0, 0))
    screen.blit(frame, (0,0))
    pygame.display.update()
