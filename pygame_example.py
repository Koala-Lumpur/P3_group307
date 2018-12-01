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
# An array - inside the [] we call the wall constructor in the Wall class (x, y pos and x, y scale for each wall)
# The for loop makes it called 11 times and adds it to the array
walls = [wall.Wall() for i in range(10)]
# Initializing pygame-s font, so we can display the FPS (necessary for displaying any text)
pygame.font.init()
# Defining a new font object (first constructor the font type, none = pygame default font, second is the font size = 30)
font = pygame.font.Font(None, 30)
# Used for limiting and getting the FPS
clock = pygame.time.Clock()
# Returns the number (in miliseconds) since pygame.init was called (before it's initialized it is zero)
last_frame = pygame.time.get_ticks()
speed_multiplier = 1
line_x = 197
line_y = 930
line_w = 1531
line_h = 46
# initalizes pygame so we can call pygame methods
pygame.init()
# (0, 0) means it has the same resolution as the screen
screen = pygame.display.set_mode((0, 0))
# Window label (the name of the window)
pygame.display.set_caption('Obstacle Course simulator 2018')
# Maybe this isn't needed
pygame.display.toggle_fullscreen()
# Loading the background image -
# .convert() creates a new copy of the surface with the pixel format changed (it boosts FPS)
background = pygame.image.load("background.jpg").convert()
wall = pygame.image.load("wall.jpeg").convert()
line = pygame.image.load("line.png").convert_alpha()
# mask.from_surface is a pygame method - sorts out all the transparent pixels
# We can use collision that ignores transparent pixels
wall_mask = pygame.mask.from_surface(wall)
#wall = pygame.transform.scale(wall, (wall.get_width()/3, wall.get_height()/3))

# This doesn't do anything at the moment
class my_thread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        '''
        update()


def update():
    while True:
    '''


update_thread = my_thread(1, "update_thread")
update_thread.start()


# Main loop
while True:
    # Setting the max FPS
    clock.tick(60)
    # Returns the time in milliseconds since pygame was initialized
    start = pygame.time.get_ticks()
    # The event loop - An open loop that makes the game continuously run (it's a necessity)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    # Once the escape key is hit, pygame.QUIT is called - which closese the whole game
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            break
    # The blit function is called on the screen object
    # (first parameter - what we want blited, second parameter - pixel pos)
    # Blitting is putting something on the screen - in this case we are visualizing the background
    # (0, 0) is the anchor point of an image
    screen.blit(background, [0, 0])
    screen.blit(line, [line_x, line_y])
    # Converting the number returned from clock.get_fps()
    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
    # Rendering the FPS text
    screen.blit(fps, (50, 50))

    # Calculating delta time
    delta_time = (start - last_frame) / 1000
    # Changing last frame to the actual last frame, so we can calculate again in the next frame
    last_frame = start
    # if statement that makes the walls disappearing after they reach a certain position
    if not walls[0].x > 5000:
        screen.blit(wall, (walls[0].new_wall_pos_x*1.5, walls[0].new_wall_pos_y))
        wall = pygame.transform.smoothscale(wall, (int(walls[0].x), int(walls[0].y)))
        walls[0].new_wall_pos_x -= int(8.8 * delta_time * speed_multiplier)
        walls[0].new_wall_pos_y -= int(4.7 * delta_time * speed_multiplier)
        walls[0].x += int(18.5 * delta_time * speed_multiplier)
        walls[0].y += int(10 * delta_time * speed_multiplier)
        speed_multiplier += 1
        if walls[0].new_wall_pos_y + walls[0].y > line_y:
            wall_rect = wall.get_rect(center=(0, 0))
            line_rect = line.get_rect(center=(0, 0))
            offset_x = wall_rect.x - line_rect.x
            offset_y = wall_rect.y - line_rect.y
            wall_mask = pygame.mask.from_surface(wall)
            hit = mask_ed.overlap(wall_mask, (offset_x, offset_y))
            print(hit)
            if hit:
                print("hit")

    
    frame = ed.main()
    frame = pygame.surfarray.make_surface(frame)
    frame.convert_alpha()
    frame_x = frame.get_width()
    frame_y = frame.get_height()
    frame.set_colorkey((0, 0, 0))
    mask_ed = pygame.mask.from_surface(frame)
    screen.blit(frame, (SCREEN_WIDTH/2 - frame_x/2, SCREEN_HEIGHT/2))




    pygame.display.update()

pygame.quit()
