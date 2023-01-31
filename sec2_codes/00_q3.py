from math import *

import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *



def draw():
    glClearColor(1, 1, 1, 1)  # SECTION 2
    glClear(GL_COLOR_BUFFER_BIT)  # SECTION 2
    glLineWidth(5)  # SECTION 2

    glColor3d(0.8, 0.6, 0.8)  # set my color, 3=RGB d=double(0.0>1.0)
    # glColor3d(1, 0 ,0) # set my color, 3=RGB d=double(0.0>1.0) TODO: try glColor3ub(255, 0,0)
    # glColor3ub(255, 0,0) # set my color, 3=RGB ub=unsigned byte(0>255)
    glBegin(GL_LINE_STRIP)  # connect them as lines and close the loop # TODO: try GL_LINE_STRIP
    resolution = .001  # TODO: try 90, must be int
    r = .5

    for ang in np.arange(0, 2*pi, resolution):  # parametric form of a circle (r*cos(theta),r*sin(theta))
        x = r * cos(ang)  # pi / 180 from angle to rad
        y = r * sin(ang)  # pi / 180 from angle to rad
        glVertex2d(x, y)  # 2 = coordL , d = float point NOT DIMENSION
    glEnd()
    glFlush()

glutInit()
glutInitWindowSize(500, 500)  # Set the window's initial width & height # TODO: try commenting this
glutInitWindowPosition(1000, 100)  # position # TODO: try commenting this
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # GLUT_SINGLE:single buffer [or operator, logically and]
glutCreateWindow(b"My First OGL Program")  # action bar # TODO: try changing this
glutDisplayFunc(draw)  # main loop  # TODO: try commenting this
glutMainLoop()

# TODO: try to print any thing here? print("hello world")
