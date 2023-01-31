from OpenGL.GL import *
from OpenGL.GLUT import *


def draw1():
    glColor3f(1.0, 0.5, 1.0)
    ####################################
    # Head
    ####################################
    glBegin(GL_POLYGON)
    glVertex2d(0.2, 0.9)
    glVertex2d(-0.2, 0.9)
    glVertex2d(-0.2, 0.6)
    glVertex2d(0.2, 0.6)
    glEnd()

    ####################################
    # Nick
    ####################################
    glBegin(GL_POLYGON)
    glVertex2d(0.1, 0.6)
    glVertex2d(-0.1, 0.6)
    glVertex2d(-0.1, 0.4)
    glVertex2d(0.1, 0.4)
    glEnd()


    ####################################
    # Stomach
    ####################################
    glBegin(GL_POLYGON)
    glVertex2d(0.5, 0.4)
    glVertex2d(-0.5, 0.4)
    glVertex2d(-0.5, -0.2)
    glVertex2d(0.5, -0.2)
    glEnd()

    ####################################
    #  Left leg
    ####################################
    glBegin(GL_POLYGON)
    glVertex2d(-0.3, -0.2)
    glVertex2d(-0.5, -0.2)
    glVertex2d(-0.5, -0.5)
    glVertex2d(-0.3, -0.5)
    glEnd()

    ####################################
    # right leg
    ####################################
    glBegin(GL_POLYGON)
    glVertex2d(0.5, -0.2)
    glVertex2d(0.3, -0.2)
    glVertex2d(0.3, -0.5)
    glVertex2d(0.5, -0.5)
    ############
    # BAD POLYGON
    # TODO : try this bad polygon
    ############
   # glVertex2d(0.3, -0.2)
    #glVertex2d(0.5, -0.2)
    #glVertex2d(0.3, -0.5)
    #glVertex2d(0.5, -0.5)
    ############
    glEnd()

    ####################################
    # right arm
    ####################################
    # # 6: right arm
    glBegin(GL_LINES)
    glVertex2d(0.5, 0.3)
    glVertex2d(0.7, -0.2)
    glEnd()

    ####################################
    # left arm
    ####################################
    # 7: left arm
    glBegin(GL_LINES)
    glVertex2d(-0.5, 0.3)
    glVertex2d(-0.7, -0.2)
    glEnd()

    glFlush()


glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"My First OGL Program")
glutDisplayFunc(draw1)
glutMainLoop()
