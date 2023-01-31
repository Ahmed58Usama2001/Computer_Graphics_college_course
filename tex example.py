from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame

MILLISECONDS = 1000

"""
Texture steps (init)
1) glEnable(GL_TEXTURE_2D)
2) pygame.image.load("1.png")
3) pygame.image.tostring(image, "RGBA", True)
4) glGenTextures(len(images), texture_names) # create identifiers for textures
5) glBindTexture(GL_TEXTURE_2D, texture_name) # modify THIS IDENTIFIER
6) glTexParameterf (many of those) # set the parameters
7) glTexImage2D # feed the binary image to opengl
              (Usage)
1) glBindTexture(GL_TEXTURE_2D, texture_name) # use THIS IDENTIFIER
2) glTexCoord(0, 0) repeat this
"""


def my_init():
    loadTextures()


texture_names = [0]  # TODO IMPORTANT must be numbers


def texture_setup(texture_image_binary, texture_name, width, height):
    """  Assign texture attributes to specific images.
    """
    glBindTexture(GL_TEXTURE_2D, texture_name)  # texture init step [5]

    # texture init step [6]
    # affects the active selected texture which is identified by texture_name
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)  # GL_MIRRORED_REPEAT , GL_CLAMP_TO_EDGE, GL_CLAMP_TO_BORDER
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    # END: texture init step [6]

    glTexImage2D(GL_TEXTURE_2D,
                 0,  # mipmap
                 3,  # Bytes per pixel
                 width, height,
                 0,  # Texture border
                 GL_RGBA,  # RGBA Exactly as in  pygame.image.tostring(image, "RGBA", True)
                 GL_UNSIGNED_BYTE,
                 texture_image_binary)  # texture init step [7]


def loadTextures():
    """  Open images and convert them to "raw" pixel maps and
             bind or associate each image with and integer refernece number.
    """
    glEnable(GL_TEXTURE_2D)  # texture init step [1]
    # Load images from file system
    images = []  # texture init step [2]
    images.append(pygame.image.load("wall.png"))  # repeat this for more images

    # Convert images to the type needed for textures
    textures = [pygame.image.tostring(image, "RGBA", True) # TODO change True to False
                for image in images]  # texture init step [3]

    # Generate textures names from array
    glGenTextures(len(images), texture_names)  # texture init step [4]

    # Add textures to openGL
    for i in range(len(images)):
        texture_setup(textures[i],  # binary images
                      texture_names[i],  # identifiers
                      images[i].get_width(),
                      images[i].get_height())


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)  # TODO IMPORTANT

    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture_names[0])  # repeat this if you want to bind another texture
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)  # TODO IMPORTANT: glTexCoord2f must come first before glVertex2d
    glVertex2d(-1, .9)

    glTexCoord2f(1, 1)
    glVertex2d(1, 1)

    glTexCoord2f(1.0, 0)
    glVertex2d(1, -1)

    glTexCoord2f(0, 0)
    glVertex2d(-1, -1)

    glEnd()

    glPopMatrix()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"tex example")
my_init()
glutDisplayFunc(draw)

glutMainLoop()
