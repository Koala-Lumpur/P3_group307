import pygame
import numpy as np
import edge_detection as ed
import background_subtraction as bs
import cv2
import time
import threading
import wall

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BLACK = (0,0,0)
WHITE = (255,255,255)
walls = [wall.Wall() for i in range(10)]
pygame.font.init()
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
last_frame = pygame.time.get_ticks()
speed_multiplier = 1

pygame.init()



screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('WHat is thiis')
pygame.display.toggle_fullscreen()

background = pygame.image.load("background.jpg")
wall = pygame.image.load("wall.jpeg")
#wall = pygame.transform.scale(wall, (wall.get_width()/3, wall.get_height()/3))

class my_thread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        update()


def update():
    while True:
        fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        screen.blit(fps, (50, 50))


update_thread = my_thread(1, "update_thread")
update_thread.start()


while True:
    clock.tick(20)
    start = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            break
    screen.blit(background, [0, 0])
    delta_time = (start - last_frame) / 1000
    last_frame = start
    if not walls[0].x > 2000:
        screen.blit(wall, (walls[0].new_wall_pos_x, walls[0].new_wall_pos_y))
        wall = pygame.transform.smoothscale(wall, (int(walls[0].x), int(walls[0].y)))
        walls[0].new_wall_pos_x -= 8.8 * delta_time * speed_multiplier
        walls[0].new_wall_pos_y -= 4.7 * delta_time * speed_multiplier
        walls[0].x += 18.5 * delta_time * speed_multiplier
        walls[0].y += 10 * delta_time * speed_multiplier
        speed_multiplier += 1

    '''
    frame = bs.main()
    frame = pygame.surfarray.make_surface(frame)
    frame_x = frame.get_width()
    frame_y = frame.get_height()
    frame.convert_alpha()
    frame.set_alpha(128)
    frame.set_colorkey((0, 0, 0))
    screen.blit(frame, (SCREEN_WIDTH/2 - frame_x/2, SCREEN_HEIGHT/2))
    '''

    pygame.display.update()

pygame.quit()
