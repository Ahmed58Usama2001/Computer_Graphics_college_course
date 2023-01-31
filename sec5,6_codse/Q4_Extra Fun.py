from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import Q1


def init_projection_plus_camera():
    # invoked only once at the beginning
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 30)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10, 10, 10,
              0, 0, 0,
              0, 1, 0)


theta = 0
forward = True
shift = 0


def draw():
    global theta
    global forward
    global shift

    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    # as if we are in identity and then gluLookAt is configured
    Q1.draw_axes()  # drawing axes doesn't affect the modelview matrix, no need to load identity

    # z(blue) >>> left - right
    # y(green) >>> top - bottom
    # x(red) >>> front - back
    # ######################
    glPushMatrix()  # Q4 <<<<<<
    glTranslate(0, 0, shift)
    glRotate(90, 0, -1, 0)  # around y axis
    draw_car(theta)
    glPopMatrix()  # Q4 >>>>>>
    # # # # ######################
    glPushMatrix()  # Q4 <<<<<<
    glTranslate(shift, 0, 0)
    draw_car(theta)
    glPopMatrix()  # Q4 >>>>>>
    # ######################
    glPushMatrix()  # Q4 <<<<<<
    glTranslate(0, shift, 0)
    glRotate(90, 0, 0, 1)
    draw_car(theta)
    glPopMatrix()  # Q4 >>>>>>
    # ######################

    glutSwapBuffers()

    theta = theta + (0.5 if forward else -.5)
    shift = shift + (0.01 if forward else -.01)

    if shift >= 5:
        forward = False

    if shift <= -5:
        forward = True

    # as if we are back to identity, gluLookAt is configured


def draw_car(theta):
    glColor3f(1, 0, 0)
    #########################################
    ######## bottom cube
    glPushMatrix()  # Q4
    glScale(4, 1, 2)
    glutWireCube(1)
    glPopMatrix()  # Q4
    #########################################
    ########## top cube
    glPushMatrix()  # Q4
    glTranslate(0, 1 - .15, 0)
    glScale(2, 1, 1.5)
    glutWireCube(1)
    glPopMatrix()  # Q4
    #########################################
    ############# wheels
    glColor3f(0, 0, 1)

    draw_wheel_Q4(loc_x=+2, loc_y=-0.5, loc_z=-1, theta=theta)  # right front wheels
    draw_wheel_Q4(loc_x=-2, loc_y=-0.5, loc_z=-1, theta=theta)  # right rear wheels
    draw_wheel_Q4(loc_x=+2, loc_y=-0.5, loc_z=1, theta=theta)  # left front wheels
    draw_wheel_Q4(loc_x=-2, loc_y=-0.5, loc_z=1, theta=theta)  # left rear wheels
    #########################################
    ############# headlight bulbs
    glColor3f(1, 1, 0)
    draw_headlight_bulb_Q4(loc_x=+2, loc_y=0, loc_z=-.5)  # right bulb
    draw_headlight_bulb_Q4(loc_x=+2, loc_y=0, loc_z=+.5)  # left bulb
    #########################################


def draw_wheel_Q4(loc_x, loc_y, loc_z, theta):
    glPushMatrix()  # Q4
    glTranslate(loc_x, loc_y, loc_z)
    glRotate(theta, 0, 0, -1)
    glutWireTorus(0.15, 0.35, 10, 12)
    glPopMatrix()  # Q4


def draw_headlight_bulb_Q4(loc_x, loc_y, loc_z):
    glPushMatrix()  # Q4
    glTranslate(loc_x, loc_y, loc_z)
    glScale(.2, 3, 3)
    glutWireSphere(0.1, 20, 20)
    glPopMatrix()  # Q4


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
glutPositionWindow(1200, 200)
init_projection_plus_camera()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
