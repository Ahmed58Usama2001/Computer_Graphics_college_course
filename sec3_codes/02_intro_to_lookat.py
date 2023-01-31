from time import sleep

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw1():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3d(1.0, 0.0, 1.0)
    ########################################
    ########################################
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # gluPerspective(20, 1, .01, 10)  # TODO: replace .01 by 0 and stop crying :(
    #
    # glMatrixMode(GL_MODELVIEW)  # To operate on Model-View matrix
    # glLoadIdentity()

    ##### try one of those four
    # gluLookAt(0, 0, -5, 0, 0, 0, 0, 1, 0)  # try this
    # gluLookAt(0, -2.25, -5, 0, 0, 0, 0, 1, 0)  # or this
    # gluLookAt(0, -5, -5, 0, 0, 0, 0, 1, 0)  # or this
    # gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)  # [default] from 0 to -1
    ########################################
    ########################################
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 3) # TODO -1 at z here makes you see behind your back
    #
    glMatrixMode(GL_MODELVIEW)  # To operate on Model-View matrix
    glLoadIdentity()

    # try only one of those three
    # gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)  # [default] from 0 to -1, TODO: this is not intuitive if you visualize it
    # gluLookAt(0, 0, +1, 0, 0, 0, 0, 1, 0) # same effect as [default] from 1 to 0
    # gluLookAt(0, 0, 0, 0, 0, 1, 0, 1, 0)  # from 0 to 1, enable GL_DEPTH_TEST and you will see the blue triangle
    ########################################
    ########################################

    # they are ordered to look wrong if glEnable is false
    glColor3f(0.0, 0.0, 1.0)  # blue
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 1)
    glVertex3f(.5, 0, 1)
    glVertex3f(0, .5, 1)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)  # green
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(.1, 0, 0)
    glVertex3f(0, .1, 0)
    glEnd()

    glFlush()


glutInit()
glutInitWindowSize(600, 600)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow(b"Two triangles in 3D")
glEnable(GL_DEPTH_TEST)
glutDisplayFunc(draw1)
glutMainLoop()
