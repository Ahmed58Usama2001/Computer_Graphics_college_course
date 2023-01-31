from OpenGL.GL import *
from OpenGL.GLUT import *

def draw():
    glutWireTeapot(.5)  # draw teapot, internally flushed
    glFlush()
    print("inside draw1")

# boilerplate
glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow("My First OGL Program")
glutDisplayFunc(draw)
glutMainLoop()