"""   Lec6 prog.1 

Author:  de Fine 
================================ 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 


def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """ 
        glClearColor(0.0, 0.0, 0.0, 0.0) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() # not necessary
        gluPerspective(120.0, Width/Height, 0.1, 100.0)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity() # not necessary
        glEnable(GL_DEPTH_TEST) # try this
        


def DrawGLScene(): 
        """ Specification of the line position and color. 
        """      
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

        
        glTranslate(0.0,0.0,-6.0)


        glColor( 1.0,1.0,0.0 ) # Yellow
        glBegin(GL_QUADS) 
        glVertex(-0.5, -0.5, -0.5) # screen coord = -0.8 (for example)-->أنا معرفش السكرين كوأورديناتس أنا عارف الوورلد بس
        glVertex(0.5, -0.5, -0.5)
        glVertex(0.5, 0.5, -0.5)
        glVertex(-0.5, 0.5, -0.5) 
        glEnd()


        glColor( 1.0,0.0,0.0 ) # Red
        glBegin(GL_QUADS) 
        glVertex(-0.5, -0.5,-1.0) # screen coord = -0.25 (for example)-->أنا معرفش السكرين كوأورديناتس أنا عارف الوورلد بس
        glVertex(0.5, -0.5,-1.0)
        glVertex(0.5, 0.5,-1.0)
        glVertex(-0.5, 0.5,-1.0) 
        glEnd()
        
        glFlush()
        
 
def main(): 
        """ Main Program. 
        """      
        glutInit() 
        glutInitWindowSize(500,500)           # Width,Height. The line gets scaled to the window. 
        glutInitWindowPosition(10,30)      # Controls where the window starts - top-left corner of screen. 
        glutInitDisplayMode(GLUT_DEPTH)
        glutCreateWindow(b'Depth Buffer') 
        glutDisplayFunc(DrawGLScene)   # Drawing. 
        InitGL(5, 5)                                    # Starting position of window on computer screen (top-left corner). 
        glutMainLoop() 
 
main()
