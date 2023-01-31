from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import math

FILL_MODE = GL_POLYGON  # TODO: this works for the figure on the left
FILL_MODE = GL_LINE_LOOP  # TODO: this works for the figure on the right


def draw_circle(r, xc=0.0, yc=0.0, st_theta=0, end_theta=360):
    # draw a circle as in 00_q3.py
    glBegin(GL_POLYGON)
    for theta in np.arange(st_theta, end_theta, 0.01):
        x = r * math.cos(theta * math.pi / 180) + xc
        y = r * math.sin(theta * math.pi / 180) + yc
        glVertex2d(x, y)
    glEnd()


def solve_for_line_at_x(p1, p2, at_x):
    # sourcery skip: inline-immediately-returned-variable
    """
    Solves for at_x for a line formed by p1,p2 using
                    y = m*x +c
    :param p1: a tuple of the form (p1_x, p1_y)
    :param p2: a tuple of the form (p2_x, p2_y)
    :param at_x: the target point to solve for x at
    :return: the value of y for the x given as at_x
    """
    p1_x, p1_y, p2_x, p2_y = p1[0], p1[1], p2[0], p2[1]

    m = (p2_y - p1_y) / (p2_x - p1_x)  # this is the slope
    c = p1_y - m * p1_x  # intercept

    y_solved = at_x * m + c
    return y_solved


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()  # TODO try commenting this
    glColor3f(.0, 0., .0)

    ###########################
    # 1: head
    draw_circle(r=.2, xc=0, yc=.57)
    ###########################
    # 2: stomach
    glBegin(FILL_MODE)
    glVertex2d(0.15, 0.4)
    glVertex2d(-0.15, 0.4)
    glVertex2d(-0.5, -0.5)
    glVertex2d(0.5, -0.5)
    glEnd()
    ###########################
    # 3: right arm
    glBegin(GL_LINES)
    ##########
    #glVertex2d(0.15, 0.3)  # TODO: try this, a fixed point
    ##########
    # TODO: try this, a solved point
    p1, p2 = (.15, .4), (.5, -.5)  # the two right points of the trapezoid
    x = .18
    y = solve_for_line_at_x(p1, p2, x)
    glVertex2d(x, y)
    ##########
    glVertex2d(0.7, -0.2)
    glEnd()
    ###########################

    ###########################
    # 4: left arm
    glBegin(GL_LINES)
    ##########
    # glVertex2d(-0.15, 0.3)  # TODO: try this, a fixed point
    ##########
    # or try this
    # y = m*x +c
    p1, p2 = (-.15, .4), (-0.5, -0.5)  # the two left points of the trapezoid
    x = -.18
    y = solve_for_line_at_x(p1, p2, x)
    glVertex2d(x, y)
    ##########
    glVertex2d(-0.7, -0.2)
    glEnd()
    ###########################

    glScale(.7, 1, 1)  # TODO: try commenting this
    # 5: left leg
    glBegin(FILL_MODE)
    glVertex2d(-0.3, -0.5)
    glVertex2d(-0.5, -0.5)
    glVertex2d(-0.5, -0.9)
    glVertex2d(-0.3, -0.9)
    glEnd()
    ###########################
    # 6: right leg
    glBegin(FILL_MODE)
    glVertex2d(0.5, -0.5)
    glVertex2d(0.3, -0.5)
    glVertex2d(0.3, -0.9)
    glVertex2d(0.5, -0.9)
    glEnd()
    ###########################

    # TODO: EYES
    # glPointSize(10)
    # glBegin(GL_POINTS)
    # glVertex2d(2, 0)
    # glEnd()
    ###########################
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Useless Figure")  # make it useful :3 ?
glutDisplayFunc(draw)

glutMainLoop()
