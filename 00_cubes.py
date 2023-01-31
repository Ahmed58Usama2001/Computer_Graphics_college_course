"""   ch8 No.5 
Objective: Construct a general cube. Demonstrate independent rotation of multiple 
instances of the cubes. 

keywords: opengl, points, lines, variable cube, independent rotation 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: A wire cube is defined interms of variables inside vertices. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
"""
from time import sleep

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

x0 = 0  # Line start .
y0 = 0
z0 = 0
rangle = 0.0


def init_my_scene(Width, Height):
    """  initial parameters. This is called right after the OpenGL window is created. 
    """
    ###############################################################################
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear background to black .
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset projection matrix.
    ###########################
    ####  use one of them #####
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    ###########################
    #glOrtho(-2, 2, -2, 2, -5, 5)
    ###############################################################################
    glMatrixMode(GL_MODELVIEW)


def draw_cube(x0, y0, z0, edge_length):
    """ Specification of the line and point positions and their color.
    a cube consists of 8 points
    THIS CUBE HAS TO BE CENTERED AT THE ORIGIN! TODO: WHY?--> for the transformatiom to be done on the origin
    x0              , y0              , z0                ###### 1
    x0              , y0 + edge_length, z0                ###### 2
    x0 + edge_length, y0 + edge_length, z0                ###### 3
    x0 + edge_length, y0              , z0                ###### 4

    x0              , y0              , z0 + edge_length  ###### 5
    x0              , y0 + edge_length, z0 + edge_length  ###### 6
    x0 + edge_length, y0 + edge_length, z0 + edge_length  ###### 7
    x0 + edge_length, y0              , z0 + edge_length  ###### 8

    TODO: for each side how many values are common in each transition?-->the two values of x and y the only difference is in the value of z
    """
    ######################################################################
    ### far side has 1,2,3,4 points
    ##############
    glColor3f(1.0, 0.0, 0.0)  # red
    glLineWidth(8.0)
    glBegin(GL_LINE_LOOP)
    glVertex3f(x0, y0, z0)  # 1
    glVertex3f(x0, y0 + edge_length, z0)  # 2
    glVertex3f(x0 + edge_length, y0 + edge_length, z0)  # 3
    glVertex3f(x0 + edge_length, y0, z0)  # 4
    glEnd()
    ######################################################################
    ### near side has 5,6,7,8 points
    ##############
    glLineWidth(2.0)
    glColor3f(0.0, 0.0, 1.0)  # ~ blue
    glBegin(GL_LINE_LOOP)
    glVertex3f(x0, y0, z0 + edge_length)  # 5
    glVertex3f(x0, y0 + edge_length, z0 + edge_length)  # 6
    glVertex3f(x0 + edge_length, y0 + edge_length, z0 + edge_length)  # 7
    glVertex3f(x0 + edge_length, y0, z0 + edge_length)  # 8
    glEnd()
    # ######################################################################
    ### connect far and near sides
    ### 1,2,3,4 => 5,6,7,8
    ### (1, 5) & (2, 6) & (3, 7) & (4, 8)
    ##############
    ##################### connect 1 and 5
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(x0, y0, z0)  # 1
    glVertex3f(x0, y0, z0 + edge_length)  # 5
    glEnd()
    # ##################### connect 2 and 6
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(x0, y0 + edge_length, z0)  # 2
    glVertex3f(x0, y0 + edge_length, z0 + edge_length)  # 6
    glEnd()
    # ##################### connect 3 and 7
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(x0 + edge_length, y0 + edge_length, z0)  # 3
    glVertex3f(x0 + edge_length, y0 + edge_length, z0 + edge_length)  # 7
    glEnd()
    # ##################### connect 4 and 8
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(x0 + edge_length, y0, z0)  # 4
    glVertex3f(x0 + edge_length, y0, z0 + edge_length)  # 8
    glEnd()
    # ######################################################################
    # draw the corners of the the far side
    ##############
    glPointSize(20.0)
    glColor3f(72 / 255.0, 0, 1.0)
    glBegin(GL_POINTS)  # Every vertex specified is a point.
    glVertex3f(x0, y0, z0)  # 1
    glVertex3f(x0, y0 + edge_length, z0)  # 2
    glVertex3f(x0 + edge_length, y0 + edge_length, z0)  # 3
    glVertex3f(x0 + edge_length, y0, z0)  # 4
    glEnd()
    # ######################################################################
    # draw the corners of the the near side
    glPointSize(12.0)
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POINTS)
    glVertex3f(x0, y0, z0 + edge_length)  # 5
    glVertex3f(x0, y0 + edge_length, z0 + edge_length)  # 6
    glVertex3f(x0 + edge_length, y0 + edge_length, z0 + edge_length)  # 7
    glVertex3f(x0 + edge_length, y0, z0 + edge_length)  # 8
    glEnd()
    # ######################################################################
    # # TODO: for fun :D--> a teapot is drawn at the origin then translated to the main corner of the cube
    glTranslatef(x0, y0, z0)  # Shift to convenient position.
    glutWireTeapot(.1)


def DrawGLScene():
    """ Specification of the line and point positions and their color. 
    """
    global rangle

    glClear(GL_COLOR_BUFFER_BIT)  # Clear screen and depth buffer.

    ###################################################################################
    # # TODO: draw some points, comment the code for cubes if you want to see this
    glPointSize(12.0)
    glLoadIdentity()
    glColor3f(0, 1, 1)
  #  glBegin(GL_POINTS)
    # try one of those vertices
    #glVertex3f(0, 0, -5)  # TODO: try this and you will see the point, why? it layes in the frustm from -0.1 : -100
   # glVertex3f(0, 0, 0)  # TODO: try this, you will see nothing, why?  it layes outside the frustm from -0.1 : -100
    # # glVertex3f(0, 0, -100)  # TODO: try this and you will see the point, why? it layes in the frustm from -0.1 : -100
    # glVertex3f(0, 0, -101)  # TODO: try this, you will see nothing, why?it layes outside the frustm from -0.1 : -100
   # glEnd()
    ###################################################################################
    # ########################################
    size = [1.0, 1.0, 1.0]  # Change size if desired.
    location = [0.0, 0.0, -5]
    # Arrays of transformations to be done
    # ########################################
    # first cube, rotate around x
    # ########################################
    glLoadIdentity()
    glTranslatef(location[0], location[1], location[2])  # Shift to convenient position.
    glScale(size[0], size[1], size[2])  # Change size if desired.
    glRotatef(rangle, 1.0, 0.0, 0.0)  # Rotate cube around X.
    draw_cube(-1.0, -1.0, -1.0, 2.0)  # Largest cube.
    # ########################################
    # # middle cube, rotate around y
    # ########################################
    glLoadIdentity()
    glTranslatef(location[0], location[1], location[2])  # Shift to convenient position.
    glScale(size[0], size[1], size[2])  # Change size if desired.
    glRotatef(rangle, 0.0, 1.0, 0.0)  # Rotate cube around y.
    draw_cube(-0.9, -0.9, -0.9, 1.8)  # Intermediate size cube.
    ######
    # TODO: try those points with the middle cube but replacing z0 by .9 instead of -.9
    # glPointSize(15)
    # glBegin(GL_POINTS)
    # glColor3f(1, 0, 0)
    # glVertex3f(0, 0, -.9 + 1.8)
    # glColor3f(0, 1, 0)
    # glVertex3f(0, 0, -.9)
    # glColor3f(0, 0, 1)
    # glVertex3f(0, 0, 0)
    # glEnd()
    ######
    # ######################################
    #  last cube, rotate around z
    # ######################################
    glLoadIdentity()
    # gluLookAt(0, 0, 15, 0, 0, 0, 0, 1, 0) # try this
    glTranslatef(location[0], location[1], location[2])  # Shift to convenient position.
    glScale(size[0], size[1], size[2])  # Change size if desired.
    glRotatef(rangle, 0.0, 0.0, 1.0)  # Rotate cube around z.
    draw_cube(-0.8, -0.8, -0.8, 1.6)  # Smallest cube.
    #######################################
    ###################################################################################
    rangle += 0.01

    glutSwapBuffers()


# ==============================================================
def main():
    """ Specification of the line and point positions and their color. 
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"Perspective: 45.0, float(Width)/float(Height), 0.1, 100.0")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    init_my_scene(1000, 1000)
    glutMainLoop()


main()
