

from OpenGL.GL import *
from OpenGL.GLUT import *


def draw1():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(1.0, 0.0, 1.0)

    glMatrixMode(GL_MODELVIEW)  # To operate on Model-View matrix
    glLoadIdentity()
    # #############################################
    # a) question 5, sheet 1
    # glScale(3, 1, 1)
    # glTranslate(0.0, -0.7, 0)
    # glRotate(120.0, 0.0, 0.0, 1.0)
    # #############################################
    # b) question 5, sheet 1
    # glTranslate(0.0, -0.7, 0)
    # glRotate(120.0, 0.0, 0.0, 1.0)
    # glScale(3, 1, 1)
    # #############################################
    # c) question 5, sheet 1
   # glRotate(120.0, 0.0, 0.0, 1.0)
   # glTranslate(0.0, -0.7, 0)
    #glScale(3, 1, 1)
    # #############################################
    glutWireTeapot(0.1)
    glFlush()

glutInit()
glutInitWindowSize(600, 600)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Teapot with Transformation")
glutDisplayFunc(draw1)
glutMainLoop()

# Transformations in a, b, and c are not equivalent, because matrix multiplication is not commutative.
