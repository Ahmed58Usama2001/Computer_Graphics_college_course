from OpenGL.GL import *
from OpenGL.GLUT import *

rangle = 0

def draw():
    global rangle

    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(0.0, 0.8, 1.0)

    glMatrixMode(GL_MODELVIEW)  # To operate on Model-View matrix
    glLoadIdentity()  # TODO : comment this

    glRotate(rangle, 0, 0, 1)  # rotate around z by 60 # counterclockwise

    glBegin(GL_POLYGON)
    glVertex2d(-0.5, -0.5)
    glVertex2d(0.5, -0.5)
    glVertex2d(0.5, 0.5)
    glVertex2d(-0.5, 0.5)
    glEnd()
   

    rangle += .01  # TODO: if it's to fast try .0001 (YOU HAVE A NICE GPU)

    glutSwapBuffers()


# boilerplate
glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow("My First OGL Program")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()



###############################
# RECIPE FOR ANIMATION
# 1) replace GLUT_SINGLE >> GLUT_DOUBLE
# 2) replace glFlush >> glutSwapBuffers
# 3) use glutIdleFunc(draw_function)
# 4) do some transformations !
###############################
