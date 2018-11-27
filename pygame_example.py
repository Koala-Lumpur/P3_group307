import pygame
import edge_detection as ed
import background_subtraction as bs
import cv2

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BLACK = (0,0,0)
WHITE = (255,255,255)
wall_pos_x = 917
wall_pos_y = 497
new_wall_pos_x = wall_pos_x
new_wall_pos_y = wall_pos_y
x = 87
y = 86



pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('WHat is thiis')
pygame.display.toggle_fullscreen()

background = pygame.image.load("background.jpg")
wall = pygame.image.load("wall.jpeg")
#wall = pygame.transform.scale(wall, (wall.get_width()/3, wall.get_height()/3))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            break
    screen.blit(background, [0, 0])
    #screen.blit(wall, (new_wall_pos_x, new_wall_pos_y))
    #wall = pygame.transform.scale(wall, (x, y))
    new_wall_pos_x -= 0.75
    new_wall_pos_y -= 0.25
    x += 1
    y += 1
    frame = bs.main()
    frame = pygame.surfarray.make_surface(frame)
    frame_x = frame.get_width()
    frame_y = frame.get_height()
    frame.convert_alpha()
    frame.set_alpha(128)
    frame.set_colorkey((0, 0, 0))
    screen.blit(frame, (SCREEN_WIDTH/2 - frame_x/2, SCREEN_HEIGHT/2))
    pygame.display.update()

pygame.quit()
