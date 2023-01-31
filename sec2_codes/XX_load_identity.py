from OpenGL.GL import *
from OpenGL.GLUT import *

def draw():
    glClearColor(1, 1, 1, 1)  # SECTION 2
    glClear(GL_COLOR_BUFFER_BIT)  # SECTION 2

    glColor3d(0.0, 0.8, 1.0)
    glMatrixMode(GL_MODELVIEW)  # To operate on Model-View matrix
    glLoadIdentity()  # TODO : comment this
    # print("glLoadIdentity\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    glRotate(30, 0, 0, 1)  # rotate around z by 60 # counterclockwise
    print("glRotate\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    #################################
    glBegin(GL_POLYGON)
    glVertex2d(-0.5, -0.5)
    glVertex2d(0.5, -0.5)
    glVertex2d(0.5, 0.5)
    glVertex2d(-0.5, 0.5)
    glEnd()
    glFlush()



# boilerplate
glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow("My First OGL Program")
glutDisplayFunc(draw)
glutMainLoop()