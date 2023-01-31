"""   Lec5 prog.3  
Program name: opengl_wirecube_1.py 
Objective: Simplified Example. 

keywords: opengl, wirecube 
============================================================================79 


Author:  De Fine 
================================ 
""" 

from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 

def init(): 
   glClearColor(1.0, 1.0, 1.0, 0) 

   # We don't modify GL_PROJECTION matrix via commands, so it equals identity matrix by default (i.e. the visible area is from -1 to +1 in u,v,w Camera axes)
   # If the camera coordinates inbetween -1,+1 in u,v,w axes , the point is visible
   
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()   
   gluLookAt(0.2,0.1,0.1, 0,0,0,  0,1,0) # try this
   #gluLookAt(2,1,1, 0,0,0,  0,1,0) # OR try this (The distance between camera and origin is sqrt(6), so the cube is outside its unit cube/frustum)
   


def display_1(): 
   glClear(GL_COLOR_BUFFER_BIT) 
   glColor(1.0, 0.0, 0.0)

   
 #  glTranslate(0,0,1.6) # try this (all points of the cube are outside the unit cube/frustum where (w > 1), (w < -1) respectively
  # glRotate(30,1,0,0) # try this
   #glRotate(2,0,1,0) # try this
   
   
   
   #gluLookAt(0.0,0.0,-0.01, 0,0,0,  0,1,0) # OR try this
   glPointSize( 15.0 ) 
   glBegin(GL_POINTS) 
   glVertex(0,0,.5) # Although this point is in back of the camera, but it is visible because it is inside the unit cube/frustum: -1 <= u <= 1 , -1 <= v <= 1 , -1 <= w <= 1
 #  glVertex(0,0,1.1) # this point is outside the unit cube/frustum: -1 <= u <= 1 , -1 <= v <= 1 , -1 <= w <= 1
   glEnd()
   
   
  # glutWireCube(1)
  # glutWireCube(2) # the camera coordinates of some points of the cube are outside the unit cube/frustum (i.e. <-1 or >1 in u,v,w camera axes)
   glFlush() 

   
glutInit( ) 
glutInitWindowSize(400, 400)
glutInitWindowPosition(0,0) # Controls where the window starts - top-left corner. 

glutCreateWindow('Wire Cube') 

glutDisplayFunc(display_1) 

init() # Any function name for initialization

glutMainLoop()
