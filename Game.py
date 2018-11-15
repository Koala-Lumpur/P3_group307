import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import EdgeDetection
import cv2
import numpy

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

def wall(image):

    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3f(-10,-10,-16)
    glTexCoord2f(0,1)
    glVertex3f(-10,10,-16)
    glTexCoord2f(1,1)
    glVertex3f(10,10,-16)
    glTexCoord2f(1,0)
    glVertex3f(10,-10,-16)
    glEnd()

def main():
    print("G-0")
    number_of_cubes = 0
    generated = False
    pygame.init()
    display = (1800, 1000)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL | pygame.OPENGLBLIT)
    print("G-1")
    # gluPerspective(45, 1, 0.05, 100)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslate(0, 0, -600)
    print("G-2")
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
    #print("G-3")

    while True:
        edges = EdgeDetection.main()
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        _, alpha = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(edges)
        edgesOnly = [b, g, r, alpha]
        img = pygame.surfarray.make_surface(edges)
        #img = pygame.Surface(img.get_size(), pygame.SRCALPHA, 32)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glTranslate(0, 0, 1)

        '''
        # Load image -- Important to load/generate the edge detection image before clearing the buffer!
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        #img = pygame.image.load("Rasmus101.png")
        width = img.get_width()
        height = img.get_height()
        textureData = pygame.image.tostring(img, "RGBA", 1)

        im = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, im)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE,
                     textureData)  # Change the first integer to 1 to hide the image while the image doesn't have transparency, and 0 to show the image

        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        '''

        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the scene
        #wall(im)
        cube(vertices)
        #print("G-5")
        for i in range(0, number_of_cubes):
            cube(cubes[i])
        #print("G-6")

        # Display image (note: random method name) -- change location in the method
        #wall(im)

        pygame.display.flip()
        pygame.time.wait(10)

main()