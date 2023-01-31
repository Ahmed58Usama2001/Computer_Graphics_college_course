import math

import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_circle(r, xc=0.0, yc=0.0, st_theta=0, end_theta=360):
    # draw a circle as in 00_q3.py
    # parametric form of a circle (r*cos(theta)+shift_x, r*sin(theta)+ shift_y)

    glBegin(GL_LINE_STRIP)
    for theta in np.arange(st_theta, end_theta, 0.01):
        x = r * math.cos(theta * math.pi / 180) + xc
        y = r * math.sin(theta * math.pi / 180) + yc
        glVertex2d(x, y)
    glEnd()


def draw():
    glClearColor(1, 1, 1, 1)  # SECTION 2
    glClear(GL_COLOR_BUFFER_BIT)  # SECTION 2
    glLineWidth(2)
    glColor3f(0, 0, 0)
    #########################
   # draw_circle(r=.8, st_theta=-30, end_theta=20)  # TODO: Try this first and comment the other parts-->draws a part from circle by these angles
    #########################
    draw_circle(r=.8)  # face
    draw_circle(r=.05, xc=0, yc=-.1)  # nose
    draw_circle(r=.05, xc=-.3, yc=.3)  # left eye
    draw_circle(r=.05, xc=+.3, yc=.3)  # right eye
    draw_circle(r=.2, xc=0, yc=-.3, st_theta=-180, end_theta=0)  # mouth, # TODO: Try reversing -180 and 0-->will draw the upper side of the circle
    #########################
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Draw face")
glutDisplayFunc(draw)
glutMainLoop()
