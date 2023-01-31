from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import Q1


#######################
# what's required in this question?
# 1) the car is supposed to move forward and backward
# 2) orthographic projection
#######################
def init_projection_Q3():  # Q3
    # invoked only once at the beginning
    # we need orthographic projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-7, 7, -7, 7, -7, 7) # TODO : replace those 5's with 3
    #glOrtho(-3, 3, -3, 3, 3, -3)  # replace those 5's with 3

    glMatrixMode(GL_MODELVIEW)


theta = 0
forward = True
shift = 0  # Q3


def reposition_camera_Q3():
    gluLookAt(1, 1, 1,
              0, 0, 0,
              0, 1, 0)
    # TODO replace 3 with 5 or 1, what do you think?


def draw():
    global theta
    global forward
    global shift  # Q3

    # clear
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    # # #########################################
    # AXES
    glLoadIdentity()
    reposition_camera_Q3()
    Q1.draw_axes()

    # z(blue) >>> left - right
    # y(green) >>> top - bottom
    # x(red) >>> front - back, here's where the car will move forward or backward

    glColor3f(1, 0, 0)
    #########################################
    ######## bottom cube
    glLoadIdentity()
    reposition_camera_Q3()  # Q3
    glTranslate(shift, 0, 0)
    glScale(4, 1, 2)
    glutWireCube(1)
    # # #########################################
    # # ########## top cube
    glLoadIdentity()
    reposition_camera_Q3()  # Q3
    glTranslate(shift, 0, 0)
    glTranslate(0, 1 - .15, 0)
    glScale(2, .7, 1.5)
    glutWireCube(1)
    # # #########################################
    # # ############# wheels
    glColor3f(0, 0, 1)
    draw_wheel_Q3(loc_x=+2 + shift, loc_y=-0.5, loc_z=-1, theta=theta)  # right front wheels
    draw_wheel_Q3(loc_x=-2 + shift, loc_y=-0.5, loc_z=-1, theta=theta)  # right rear wheels
    draw_wheel_Q3(loc_x=+2 + shift, loc_y=-0.5, loc_z=1, theta=theta)  # left front wheels
    draw_wheel_Q3(loc_x=-2 + shift, loc_y=-0.5, loc_z=1, theta=theta)  # left rear wheels
    # # #########################################
    # # ############# headlight bulbs
    glColor3f(1, 1, 0)
    draw_headlight_bulb_Q3(loc_x=+2 + shift, loc_y=0, loc_z=-.5)  # right bulb
    draw_headlight_bulb_Q3(loc_x=+2 + shift, loc_y=0, loc_z=+.5)  # left bulb
    # # #########################################
    glutSwapBuffers()

    theta = theta + (0.05 if forward else -.05)
    shift = shift + (0.001 if forward else -.001)  # Q3

    if shift >= 3:  # Q3
        forward = False

    if shift <= -3:  # Q3
        forward = True


def draw_wheel_Q3(loc_x, loc_y, loc_z, theta):
    glLoadIdentity()
    reposition_camera_Q3()
    glTranslate(loc_x, loc_y, loc_z)
    glRotate(theta, 0, 0, -1)
    glutWireTorus(0.15, 0.35, 10, 12)


def draw_headlight_bulb_Q3(loc_x, loc_y, loc_z):
    glLoadIdentity()
    reposition_camera_Q3()
    glTranslate(loc_x, loc_y, loc_z)
    glScale(.2, 3, 3)
    glutWireSphere(0.1, 20, 20)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
glutPositionWindow(500, 160)
init_projection_Q3()  # Q3
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
