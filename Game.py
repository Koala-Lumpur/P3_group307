import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import EdgeDetection

cubes = []


def generate_vertices(x, y, z, w, h, d):
    v = (
        (x + w, y, z + d),
        (x + w, y + h, z + d),
        (x, y + h, z + d),
        (x, y, z + d),
        (x + w, y, z + d),
        (x + w, y + h, z + d),
        (x, y, z + d),
        (x, y + h, z + d)
    )
    return v


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
'''
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
    
vertices4 = (
    (-1, -0.5, 170),
    (1, -0.5, 170),
    (1, -1, 170),
    (-1, -1, 170),
    (-1, -0.5, 170),
    (-1, -0.5, 170),
    (-1, -1, 170),
    (-1, -1, 170)
    )
'''

#v1 = generateVertices(-1, -1, 550, 1, 2, 5)
#v2 = generateVertices(1, 1, 500, -1, -2, 5)
#v3 = generateVertices(-1, -1, 450, 2, 0.3, 5)
#v4 = generateVertices(1, 1, 400, -2, -0.65, 5)
#v5 = generateVertices(-1, -1, 350, 1, 2, 5)
#v6 = generateVertices(1, 1, 300, -1, -2, 5)
#v7 = generateVertices(-1, -1, 250, 2, 0.3, 5)
#v8 = generateVertices(1, 1, 200, -2, -0.65, 5)

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
'''
ground_vertices = (
    (-10, -1.1, 20),
    (10, -1.1, 20),
    (-10, -1.1, -300),
    (10, -1.1, -300),
)

def ground():
    glBegin(GL_QUADS)
    for vertex in ground_vertices:
        glColor3fv((0, 0.5, 0.5))
        glVertex3fv(vertex)
    glEnd()

def set_vertices(max_distance):
    x_value_change = random.randrange(-10, 10)
    y_value_change = random.randrange(-10, 10)
    z_value_change = random.randrange(-1*max_distance, -20)

    new_vertices = []

    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[0] + y_value_change
        new_z = vert[0] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

        return new_vertices
'''


def cube(vertices):
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

    number_of_cubes = 0
    generated = False
    pygame.init()
    display = (1800,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslate(0, 0, -600)

    for i in range(600, 0, -25):
        rand = random.randint(0, 3)
        last_rand = rand
        print(number_of_cubes)
        print(rand)
        if rand == 0:
            cubes.append(generate_vertices(-1, -1, i, 1, 2, 5))
        if rand == 1:
            cubes.append(generate_vertices(1, 1, i, -1, -2, 5))
        if rand == 2:
            cubes.append(generate_vertices(-1, -1, i, 2, 0.3, 5))
        if rand == 3:
            cubes.append(generate_vertices(1, 1, i, -2, -0.80, 5))
        number_of_cubes += 1

    while True:
        EdgeDetection.main()
        '''
        if(i % 5 == 0):
            v1 = generateVertices(-1, -1, 190-i, 2, 2, 2)
            print(i)
        i += 0.5
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glTranslate(0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        cube(vertices)

        for i in range(0, number_of_cubes):
            cube(cubes[i])

        pygame.display.flip()
        pygame.time.wait(10)

main()