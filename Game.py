import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, 800),
    (1, 1, 800),
    (-1, 1, 800),
    (-1, -1, 800),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

vertices2 = (
    (-0.5, -1, 190),
    (-0.5, 1, 190),
    (-1, 1, 190),
    (-1, -1, 190),
    (-0.5, -1, 190),
    (-0.5, 1, 190),
    (-1, -1, 190),
    (-1, 1, 190)
    )

vertices3 = (
    (1, -0.5, 180),
    (1, 1, 180),
    (-1, 1, 180),
    (-1, -0.5, 180),
    (1, -0.5, 180),
    (1, 1, 180),
    (-1, -0.5, 180),
    (-1, 1, 180)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

colors = (
    (1,1,1),
    (1,1,1),
    (0.5,0.5,0.5), #Left Wall
    (1,1,1), #Front
    (0.5,0.5,0.5), #Right wall
    (0.5,0.5,0.5), #Roof
    (0,0,0), #Floor & edges?
    (0.5,0.5,0.5),
    (1,1,1),
    (0.5,0.5,0.5),
    (0.5,0.5,0.5),
    (0,0,0),
    )


def Cube(vertices):
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv((colors[x]))
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1300,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glTranslatef(0,0,0.05)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(vertices)
        Cube(vertices2)
        Cube(vertices3)
        pygame.display.flip()
        pygame.time.wait(10)


main()