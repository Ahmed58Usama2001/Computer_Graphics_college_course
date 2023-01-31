import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *

from rotating_cubes_00 import drawXYZ
# Rotation angles for each cube.
from rotating_cubes_00 import initGL

xrot1 = yrot1 = zrot1 = 0.0
xrot2 = yrot2 = zrot2 = 0.0

# Texture Names List
texture_names = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

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


def texture_setup(texture_image_binary, texture_name, width, height):
    """  Assign texture attributes to specific images.
    """
    glBindTexture(GL_TEXTURE_2D, texture_name)  # texture init step [5]

    # texture init step [6]
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
                 GL_RGBA, GL_UNSIGNED_BYTE, texture_image_binary)  # texture init step [7]


def load_and_setup(image_path, idx):
    # Load images from file system
    image = pygame.image.load(image_path)
    # Convert images to the type needed for textures
    texture = pygame.image.tostring(image, "RGBA", True)  # texture init step [3]
    texture_setup(texture, texture_names[idx], image.get_width(), image.get_height())


def load_textures():
    """  Open images and convert them to "raw" pixel maps and
             bind or associate each image with and integer refernece number.
    """
    glEnable(GL_TEXTURE_2D)  # texture init step 1

    # Generate textures names from array
    glGenTextures(len(texture_names), texture_names)  # texture init step [4]

    # Add textures to openGL [2, 3, 5 ,6 ,7]
    load_and_setup("chess.png", texture_names[0])
    load_and_setup("chess.png", texture_names[1])
    load_and_setup("chess.png", texture_names[2])
    load_and_setup("chess.png", texture_names[3])
    load_and_setup("chess.png", texture_names[4])
    load_and_setup("chess.png", texture_names[5])

    load_and_setup("1.png", texture_names[6])
    load_and_setup("2.png", texture_names[7])
    load_and_setup("3.png", texture_names[8])
    load_and_setup("4.png", texture_names[9])
    load_and_setup("5.png", texture_names[10])
    load_and_setup("6.png", texture_names[11])


def make_cube(first_index):
    """   A generic cube. A texture binding created with glBindTexture remains active until a different
            texture is bound to the same target, or until the bound texture is deleted with glDeleteTextures.
    """
    # Front Face
    glBindTexture(GL_TEXTURE_2D, texture_names[first_index])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Left

    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Right

    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)  # Top Right

    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)  # Top Left
    glEnd()

    # Back Face
    glBindTexture(GL_TEXTURE_2D, texture_names[first_index + 1])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Right
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)  # Top Left
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Left
    glEnd()

    # Top Face
    glBindTexture(GL_TEXTURE_2D, texture_names[first_index + 2])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)  # Bottom Left
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)  # Bottom Right
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)  # Top Right
    glEnd()

    # Bottom Face
    glBindTexture(GL_TEXTURE_2D, texture_names[first_index + 3])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)  # Top Right
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)  # Top Left
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right
    glEnd()

    # Right face
    glBindTexture(GL_TEXTURE_2D, texture_names[first_index + 4])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Right
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)  # Top Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)  # Top Left
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left
    glEnd()

    # Left Face
    glBindTexture(GL_TEXTURE_2D, texture_names[first_index + 5])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Left
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)  # Top Right
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left
    glEnd()

    glBindTexture(GL_TEXTURE_2D, -1)  # TODO bind to no texture


def draw():
    """   A texture binding created with glBindTexture remains active until a different texture
              is bound to the same target, or until the bound texture is deleted with glDeleteTextures.
    """
    global xrot1, yrot1, zrot1, xrot2, yrot2, zrot2
    # Clear the screen and Depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # # First textured cube.
    glLoadIdentity()  # Reset The ModelView

    glTranslatef(-2.0, 0.0, -5.0)  # Shift cube left and back. we are using the default camera 0,0,0 > 0,0,-1
    glRotatef(xrot1, 1.0, 0.0, 0.0)  # Rotate the cube on It's X axis.
    glRotatef(yrot1, 0.0, 1.0, 0.0)  # Rotate the cube on It's Y axis.
    glRotatef(zrot1, 0.0, 0.0, 1.0)  # Rotate the cube on It's Z axis.
    # glColor3f(1, 1, 0)  # Yellow
    make_cube(0)
    drawXYZ()
    xrot1 = xrot1 + 0.02  # X rotation of first cube.
    yrot1 = yrot1 - 0.01  # Y rotation
    zrot1 = zrot1 + 0.01  # Z rotation

    # # Second textured cube.
    glLoadIdentity()  # Reset The ModelView, lookat is now reset

    glTranslatef(1.5, 0.0, -5.0)  # Shift cube right and back. we are using the default camera 0,0,0 > 0,0,-1
    glRotatef(xrot2, 1.0, 0.0, 0.0)  # Rotate the cube on It's X axis.
    glRotatef(yrot2, 0.0, 1.0, 0.0)  # Rotate the cube on It's Y axis.
    glRotatef(zrot2, 0.0, 0.0, 1.0)  # Rotate the cube on It's Z axis
    # glColor3f(0, 1, 1)  # Cyan
    make_cube(6)
    xrot2 = xrot2 - .01  # X rotation of second cube.
    yrot2 = yrot2 + .02  # Y rotation
    zrot2 = zrot2 + .04  # Z rotation
    print(xrot1, yrot1, zrot1)
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 500)
    glutCreateWindow(b"Textured rotating cubes")
    load_textures()  # init the textures
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    initGL(1000, 500)
    glutMainLoop()


main()
