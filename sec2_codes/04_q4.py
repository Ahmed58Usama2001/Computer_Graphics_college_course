from math import sin

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from numpy import arange

X_LIMIT = 4
Y_LIMIT = 4


def draw_axes():
    #
    glLineWidth(2)  # line width for axes

    # horizontal axis
    glColor3f(1, 0, 0)  # red
    glBegin(GL_LINES)
    glVertex2d(-X_LIMIT, 0)
    glVertex2d(X_LIMIT, 0)
    # vertical axis
    glColor3f(0, 0, 1)  # green
    glVertex2d(0, -Y_LIMIT)
    glVertex2d(0, Y_LIMIT)
    glEnd()
    ######
    # points on axes, in black
    glPointSize(5)  # point size for point on axes
    glColor3f(0, 0, 0)
    glBegin(GL_POINTS)
    for x in np.arange(-X_LIMIT, X_LIMIT, 1):
        glVertex2d(x, 0)

    for y in np.arange(-Y_LIMIT, Y_LIMIT, 1):
        glVertex2d(0, y)
    glEnd()


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(0, 0, 0)
    ##############################
    glMatrixMode(GL_PROJECTION)
    # either 1) ortho or 2) perspective
    glLoadIdentity()  # affects GL_PROJECTION matrix
    gluOrtho2D(-X_LIMIT, X_LIMIT, -Y_LIMIT, Y_LIMIT)
    ###############################
    glMatrixMode(GL_MODELVIEW)
    # 1) MODEL : objects, world, me and you
    # 2) view : camera lookat
    glLoadIdentity()  # affects GL_MODELVIEW matrix
    ###############################

    draw_axes()

    draw_any_function()

    glFlush()


def draw_any_function():
    glLineWidth(5)
    glColor3f(0, 1, 0)  # the function will be in green
    resolution = 0.001  # TODO: change this
    # in math y = A*sin(w*t) = A*sin(2*pi*f*t)
    peak = .5  # A in the equation
    f = 2  # 2 cycles every second
    glBegin(GL_LINE_STRIP)
    for x in np.arange(0, 2, resolution): # TODO: replace (2 * np.pi) with 3 or 2
        y = peak * np.sin(2 * np.pi * f * x)
        # y = x * x # TODO: try this function
        # y = x # TODO: try this function
        glVertex2d(x, y)
    glEnd()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Equation Program")
glutDisplayFunc(draw)
glutMainLoop()
