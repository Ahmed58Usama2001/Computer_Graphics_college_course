from OpenGL.GL import *
from OpenGL.GLUT import *

# GL: graphic library: points / lines / graphics / apply linear algebra
# GLUT : GLUT stands for "GL Utilities Toolkit"
# camel case

def draw():
 
    ####################################
    # Yellow triangle
    ####################################
    glColor3d(1, 1, 0)  # yellow
    # 2 = 2 coords , d = double floating precision
    glBegin(GL_POLYGON)  # filled polygon, there's are some assumptions, you will learn more about them later
    glVertex2d(-0.5, -0.5)
    glVertex2d(0.5, -0.5)
    glVertex2d(0.5, 0.5)
    glEnd()  # TODO: try commenting this-->A bug
    ####################################

   # blue triangle
    ####################################
    # 2 = 2 coords , i = integer
    glColor3d(0, 0, 1)  # blue
    glBegin(GL_POLYGON)
    glVertex2i(0, 2)
    glVertex2i(0, 0)
    glVertex2i(1, 0)
    glEnd()  # TODO: try commenting this-->a bug
    ####################################


    # TODO: try to switch the order of triangles?-->the last one written in code is the one which will be on the top
    glFlush()  # render from the buffer # TODO: try commenting this-->my orders in code will be just in memory and will never appear on the screen
    print("hi")

glutInit() # initialize glut routines
glutInitWindowSize(500, 500)  # Set the window's initial width & height # TODO: try commenting this
glutInitWindowPosition(0, 100)  # position # TODO: try commenting this
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
# GLUT_SINGLE(use single buffer) and GLUT_RGB(use red green blue colors)
# [or operator, logically and]
# | or operator
# GLUT_SINGLE 1000000
# GLUT_RGB    0100000
# logically using GLUT_SINGLE and GLUT_RGB simultaneously
glutCreateWindow(b"My First OGL Program")  # window title # TODO: try changing this-->set the name written on the window..by commenting this no window will appear
glutDisplayFunc(draw)  # callback function to draw  # TODO: try commenting this--> draw function won`t be called
glutMainLoop() # sustaining loop, continuously monitoring events-->endless

# TODO: try to print any thing here? print("hello world")-->glutmainloop() is an infinite loop
print("hello world")