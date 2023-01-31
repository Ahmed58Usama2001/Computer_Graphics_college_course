from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

# Rotation angles for each cube.
xrot1 = yrot1 = zrot1 = 0.0
xrot2 = yrot2 = zrot2 = 0.0

"""
Depth testing (init)
1) glutInitDisplayMode(GLUT_DEPTH)
2) glEnable(GL_DEPTH_TEST)
3) glDepthFunc(GL_LESS) [optional] # The type Of depth test to do.
4) glClearDepth(1.0)  [optional] # specify the clear value for the depth buffer
            (Usage)
1) glClear(GL_DEPTH_BUFFER_BIT) # Clear the Depth buffer.
"""


def initGL(Width, Height):
    """ A general OpenGL initialization function.  Sets all of the initial parameters.
            We call this right after our OpenGL window is created.
    """
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear the background color to black.
    # glClearDepth(1)  # Clear the Depth buffer. [optional]
    # glDepthFunc(GL_LESS)  # The type Of depth test to do. [optional]
    # Leave this Depth Testing and observe the visual weirdness.
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    # Reset The Projection Matrix.
    glLoadIdentity()
    # Aspect ratio. Make window resizable.
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def make_cube():
    # Front Face

    glBegin(GL_QUADS)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Left
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Right
    glVertex3f(1.0, 1.0, 1.0)  # Top Right
    glVertex3f(-1.0, 1.0, 1.0)  # Top Left
    glEnd()

    # Back Face
    glBegin(GL_QUADS)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Right
    glVertex3f(-1.0, 1.0, -1.0)  # Top Right
    glVertex3f(1.0, 1.0, -1.0)  # Top Left
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Left
    glEnd()

    # Top Face
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left
    glVertex3f(-1.0, 1.0, 1.0)  # Bottom Left
    glVertex3f(1.0, 1.0, 1.0)  # Bottom Right
    glVertex3f(1.0, 1.0, -1.0)  # Top Right
    glEnd()

    # Bottom Face
    glBegin(GL_QUADS)
    glVertex3f(-1.0, -1.0, -1.0)  # Top Right
    glVertex3f(1.0, -1.0, -1.0)  # Top Left
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right
    glEnd()

    # Right face
    glBegin(GL_QUADS)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Right
    glVertex3f(1.0, 1.0, -1.0)  # Top Right
    glVertex3f(1.0, 1.0, 1.0)  # Top Left
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left
    glEnd()

    # Left Face
    glBegin(GL_QUADS)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Left
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right
    glVertex3f(-1.0, 1.0, 1.0)  # Top Right
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left
    glEnd()


def drawXYZ():
    glLineWidth(10)
    glBegin(GL_LINES)
    # X
    glColor3f(1, 0, 0)
    glVertex3d(-100, 0, 0)
    glVertex3d(100, 0, 0)

    # Y
    glColor3f(0, 1, 0)
    glVertex3d(0, -100, 0)
    glVertex3d(0, 100, 0)

    # Z
    glColor3f(0, 0, 1)
    glVertex3d(0, 0, -100)
    glVertex3d(0, 0, 100)

    glColor3f(1, 1, 1)
    glEnd()


def draw():
    """   A texture binding created with glBindTexture remains active until a different texture
              is bound to the same target, or until the bound texture is deleted with glDeleteTextures.
    """
    global xrot1, yrot1, zrot1, xrot2, yrot2, zrot2
    # Clear the screen and Depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # # First textured cube.
    glLoadIdentity()  # Reset The ModelView
    # gluLookAt(2, 2, 10, # TODO YOU MAY TRY THIS
    #           0, 0, -1,
    #           0, 1, 0)
    # drawXYZ() # TODO YOU MAY TRY THIS

    glTranslatef(-2.0, 0.0, -5.0)  # Shift cube left and back. we are using the default camera 0,0,0 > 0,0,-1
    glRotatef(xrot1, 1.0, 0.0, 0.0)  # Rotate the cube on It's X axis.
    glRotatef(yrot1, 0.0, 1.0, 0.0)  # Rotate the cube on It's Y axis.
    glRotatef(zrot1, 0.0, 0.0, 1.0)  # Rotate the cube on It's Z axis.
    # glColor3f(1, 1, 0)  # Yellow
    make_cube()
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
    make_cube()
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
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    initGL(1000, 500)
    glutMainLoop()


if __name__ == "__main__":
    main()
