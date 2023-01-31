"""   Lec6 prog.3  

Author:  De Fine 
================================ 
""" 

from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 

rangle = 0 # WHY global variable
zloc = 0

def init(): 
   glClearColor(1.0, 1.0, 1.0, 0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluPerspective(120,1,0.1,100) # try comment this line ; (note: znear can equal 0)
  # glOrtho(-2,2,-2,2,-3,3) # try this line ; (note:near can be negative)
   

   glMatrixMode(GL_MODELVIEW)     # try this
   glLoadIdentity()
   #gluLookAt(0.5,1.1,0, 0,0,0,  -1,0,0) # "glLoadIdentity()" in "display_1()" will remove the effect of "gluLookAt", so we must put "gluLookAt" after "glLoadIdentity()" in "display_1()"
   

   glEnable(GL_DEPTH_TEST) # try this with the colored cube below and notice the "black" (the last drawen color)

   

def display_1():
   global rangle
   global zloc
   
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # necessary to remove the previous frame
   glColor(1.0, 0.0, 0.0)

   glLoadIdentity() # necessary to remove the previous transformations
   
  # gluLookAt(0.5,1.1,0, 0,0,0,  -1,0,0) # We must put "gluLookAt" after "glLoadIdentity()", so that "glLoadIdentity()" removes the effect of "gluLookAt"
   
   
   glTranslate(0.0,0.0,zloc)
   glRotate(rangle,0,1,0) 

   # try to swap between translation and rotation
   #glRotate(rangle,0,1,0) 
  # glTranslate(0.0,0.0,-1)   
   
   
   glutWireTeapot(0.5)
  # glutSolidTeapot(0.5)
   #glutWireCube(0.5)
   
   '''
   glBegin(GL_QUADS) # use glTranslate(0.0,0.0,-2), so that the cube will be in the front of camera 
   
   glColor(0.0, 0.0, 1.0) # blue
   glVertex(1.0, 1.0, -1.0)
   glVertex(-1.0, 1.0, -1.0)
   glVertex(-1.0, 1.0, 1.0)
   glVertex(1.0, 1.0, 1.0)
    
   glColor(0.5, 0.5, 0.5) # gray
   glVertex(1.0, -1.0, 1.0)
   glVertex(-1.0, -1.0, 1.0)
   glVertex(-1.0, -1.0, -1.0)
   glVertex(1.0, -1.0, -1.0)
   
   glColor(1.0, 0.0, 1.0) # purple
   glVertex(1.0, 1.0, 1.0)
   glVertex(-1.0, 1.0, 1.0)
   glVertex(-1.0, -1.0, 1.0)
   glVertex(1.0, -1.0, 1.0)
   
   glColor(0, 1.0, 0.0) # green
   glVertex(1.0, -1.0, -1.0)
   glVertex(-1.0, -1.0, -1.0)
   glVertex(-1.0, 1.0, -1.0)
   glVertex(1.0, 1.0, -1.0)
   
   glColor(0.0, 1.0, 1.0) # Cyan
   glVertex(-1.0, 1.0, 1.0)
   glVertex(-1.0, 1.0, -1.0)
   glVertex(-1.0, -1.0, -1.0)
   glVertex(-1.0, -1.0, 1.0)
   
   glColor(0.0, 0.0, 0.0) # black (the last drawn color)
   glVertex(1.0, 1.0, -1.0)
   glVertex(1.0, 1.0, 1.0)
   glVertex(1.0, -1.0, 1.0)
   glVertex(1.0, -1.0, -1.0)

   glEnd()
   '''
   
   
   rangle = rangle+0.1
   zloc = zloc-0.0005
   glFlush() 

   
glutInit( ) 
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_DEPTH)
glutCreateWindow(b'Wire Cube') 
glutDisplayFunc(display_1)
glutIdleFunc(display_1) 
init() # Any function name for initialization
glutMainLoop()
