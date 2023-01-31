"""   Lec5 prog.1 
Program name: opengl_one_line_1.py 
Objective: Using openGL draw a single line which is specified by means of 
variables passed to a vertex 'glBegin/glEnd' set.  
 
Keywords: OpenGL, line, linewidth 
============================================================================79 


Comments: glLineWidth(float width); 
Sets the width in pixels for rendered lines; width must be greater than 0.0
and by default is 1.0. 

Author:  de Fine 
================================ 
""" 
from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*


x0 =  1.0    # Line start
y0 =  1.0
x1 = -1.0    # Line finish 
y1 =  1.0

def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """ 

        glClearColor(0.0, 0.0, 0.0, 0.0)  # Black
        #glClearColor(1.0, 0.0, 0.0, 0.0)   # try this
        
        
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() # default value of GL_PROJECTION matrix
        gluPerspective(45.0, Width/Height, 0.1, 100.0) # (note: znear can equal 0)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity() # default value of GL_MODELVIEW matrix

def any_line(x0,y0,x1,y1, R,G,B): 
        """ Specification of the line position and color. 
        """
        glColor(R,G,B)

        glBegin(GL_LINES) 

        glVertex(x0, y0,-1)
        glVertex(x1, y1,-1)

        glEnd() 

def DrawGLScene(): 
        """ Specification of the line position and color. 
        """      
        glClear(GL_COLOR_BUFFER_BIT)
      #  glTranslate(0.0,0.0,-1.5)
        #glTranslate(0.0,0.0,-1.0) # try this (the line is outside the frustum)
        #glTranslate(0.0,0.0,-20.0) # try this
        glTranslate(0.0,0.0,-99.0) # try this
      #  glTranslate(0.0,0.0,-100.0) # try this (the line is outside the frustum)
        
        glLineWidth(10)

        any_line(x0,y0,x1,y1, 1.0,0.5,0.5 ) # Our line to be drawn.

        glFlush()
        
 
def main(): 
        """ Main Program. 
        """      
        glutInit()
        glutInitWindowSize(600,600)    # Width,Height of the window. The line gets scaled to the window. 
        glutInitWindowPosition(450,120)     # Controls where the window starts - top-left corner of screen.
        glutCreateWindow('OpenGL-Python Line') 

        glutDisplayFunc(DrawGLScene)   # Drawing function

        InitGL(5, 5)  # 5,5 are the width and height of the frustum
        glutMainLoop() # starting to draw the scene and starting to call DrawGLScene( ) function
 
main()
