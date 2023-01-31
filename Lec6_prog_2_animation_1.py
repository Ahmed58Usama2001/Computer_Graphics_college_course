"""   Lec6 prog.3  

Author:  De Fine 
================================ 
""" 

from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 

scale = 1
increasing = 1
product = 1

def init(): 
   glClearColor(1.0, 1.0, 1.0, 0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
  # gluPerspective(120,1,0.1,5) # try this
   
   glMatrixMode(GL_MODELVIEW)    
  
   

def display_1():
   global scale
   global increasing
   global product
   
   glClear(GL_COLOR_BUFFER_BIT)# necessary to remove the previous frame
   glColor(1.0, 0.0, 0.0)

   glLoadIdentity() # necessary to remove the previous transformations
   #product = product * scale # comment glLoadIdentity() and uncomment these two lines
   #print('product = ',product) # scale will increase to infinity and the sphere will be so big and outside the frustum
   
   #glTranslate(0,0,-2) # Try this with gluPerspective( )
   glScale(scale,scale,scale) 
      
   glutSolidSphere(0.1,100,100) # raduis = 0.1
   
   if scale > 10: # if scale= 10 & raduis= 0.1 & projection matrix is identity, then New_raduis=scale*raduis= 1 and the sphere fills the unit cube/frustum
      increasing = 0
      
   if scale < 1:
      increasing = 1   
      
   if increasing:
      scale = scale +0.001  #0.1
   else:
      scale = scale -0.001  #0.1


   glFlush() 

   
glutInit( ) 
glutInitWindowSize(500, 500) 
glutCreateWindow(b'Wire Cube') 
glutDisplayFunc(display_1)
glutIdleFunc(display_1)
init() # Any function name for initialization
glutMainLoop()
