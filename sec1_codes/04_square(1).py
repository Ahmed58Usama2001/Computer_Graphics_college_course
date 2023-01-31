from OpenGL.GL import *
from OpenGL.GLUT import *

def draw():
    glColor3d(0.0, 0.8, 1.0)

    glMatrixMode(GL_MODELVIEW)  # To operate on Model-View matrix
    glLoadIdentity() # TODO : comment this
    #################################
    # rotete then scale
    #################################
    # print("glLoadIdentity\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    # glScale(1.5, 1, 1)  # scale on x by 1.5
    # print("glScale\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    # glRotate(60, 0, 0, 1)  # rotate around z by 60 # counterclockwise
    # print("glRotate\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    #################################
    # scale then rotete
    #################################
    print("glLoadIdentity\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    glRotate(60, 0, 0, 1)  # rotate around z by 60 # counterclockwise
    print("glRotate\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    glScale(1.5, 1, 1)  # scale on x by 1.5
    print("glScale\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    #################################
    glBegin(GL_POLYGON)
    glVertex2d(-0.5, -0.5)
    glVertex2d(0.5, -0.5)
    glVertex2d(0.5, 0.5)
    glVertex2d(-0.5, 0.5)
    glEnd()
    glFlush()
    print("ENNND")


# boilerplate
glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow("My First OGL Program")
glutDisplayFunc(draw)
glutMainLoop()