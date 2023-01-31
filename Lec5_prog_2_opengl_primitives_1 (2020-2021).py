""" Lec5 prog.2
Program name: opengl_primitives_1.py 
Objective: Show each openGL primitive using a common set of points.  
 
Keywords: OpenGL, line. strip, triangle, quad, polygon, points 
============================================================================79 


Comments: NOTE: For GL_QUADS, GL_QUAD_STRIP, and GL_POLYGON, 
all primitives must be both planar and convex. 
Otherwise, OpenGL behavior is undefined. 
The GLU library supports polygon tessellation, which allows applications to render 
filled primitives that are nonconvex or self-intersecting, or that contain holes. 

Author:  de Fine 
================================

"""

from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 


# A Zig-zag stripe of points. 
v0  =  [-1.4 ,  0.5 , 0.0 ]   
v1  =  [-1.2 , -0.5 , 0.0 ] 

v2  =  [-1.0 ,  0.5 , 0.0 ] 
v3  =  [-0.8 , -0.5 , 0.0 ] 

v4  =  [-0.6 ,  0.5 , 0.0 ] 
v5 =   [-0.4 , -0.5 , 0.0 ]  

v6  =  [-0.2 ,  0.5 , 0.0 ]   
v7  =  [ 0.0 , -0.5 , 0.0 ] 

v8  =  [0.2 ,  0.5  , 0.0 ] 
v9  = [0.4 , -0.5  , 0.0 ] 

v10  = [0.6 ,  0.5  , 0.0 ] 
v11 =  [0.8 , -0.5  , 0.0 ]  
 
v12  = [1.0 ,  0.5  , 0.0 ]   
v13  = [1.2 , -0.5  , 0.0 ] 



def vertex_set(): 
    glVertex(v0[0], v0[1], v0[2]) 
    glVertex(v1[0], v1[1], v1[2]) 
    glVertex(v2[0], v2[1], v2[2]) 
    glVertex(v3[0], v3[1], v3[2]) 
    glVertex(v4[0], v4[1], v4[2]) 
    glVertex(v5[0], v5[1], v5[2]) 
    glVertex(v6[0], v6[1], v6[2]) 
    glVertex(v7[0], v7[1], v7[2]) 
    glVertex(v8[0], v8[1], v8[2]) 
    glVertex(v9[0], v9[1], v9[2]) 
    glVertex(v10[0], v10[1], v10[2]) 
    glVertex(v11[0], v11[1], v11[2]) 
    glVertex(v12[0], v12[1], v12[2]) 
    glVertex(v13[0], v13[1], v13[2]) 


def vertex_set_polygon(): # vertices for Polygon
    
    glVertex(-1, 0, 0) 
    glVertex(-0.5, -0.5, 0) 
    glVertex(0.5, -0.5, 0) 
    glVertex(1, 0, 0) 
    glVertex(0.5, 0.5, 0) 
    glVertex(-0.5, 0.5, 0)
    
    '''
    # Unexpected behavior     
    glVertex(-0.5, -0.5, 0) 
    glVertex(0.5, -0.5, 0) 
    glVertex(-1, 0, 0)
    glVertex(1, 0, 0)
    glVertex(-0.5, 0.5, 0)
    glVertex(0.5, 0.5, 0) 
    ''' 

    
def unjoined_line(): 
    """ Joins PAIRS of unconnected segments. """ 
    glBegin(GL_LINES) 
    glColor(1.0, 0.0, 0.0)  # Red 
    vertex_set() 
    glEnd() 

def joined_line(): 
    """ Joins all points in sequence. """ 
    glBegin(GL_LINE_STRIP) 
    glColor(0.2, 0.2, 1.0)  # Blue 
    vertex_set() 
    glEnd() 

def line_loop(): 
    """ Joins all points in sequence, closing the loop. """ 
    glBegin(GL_LINE_LOOP) 
    glColor(0.0, 1.0, 1.0)  # Turquoise 
    vertex_set() 
    glEnd() 

def triangles(): 
    """ Makes triangles of groups of three. """ 
    glBegin(GL_TRIANGLES) 
    glColor(0.0, 1.0, 0.0)  # Green 
    vertex_set() 
    glEnd() 

def triangle_strip(): 
    """ First triangle using the first, second, and third vertices,
        and then another using the second, 
        third, and fourth vertices, and so on. """ 
    glBegin(GL_TRIANGLE_STRIP) 
    glColor(0.8, 1.0, 0.0)  # Orange 
    vertex_set() 
    glEnd() 

def triangle_fan(): 
    """ First triangle using the first, second, and third vertices,
        and then another using the second, 
        third, and fourth vertices, and so on. """ 
    glBegin(GL_TRIANGLE_FAN) 
    glColor(1.0, 0.8, 0.0)  # Orange 
    vertex_set() 
    glEnd() 

def quads(): 
    """ First quadrilateral using the first four vertices, 
        and then another using the next four, 
        and so on. 
    """ 
    glBegin(GL_QUADS) 
    glColor(1.0, 0.40, 0.0)  # Orange 
    vertex_set() 
    glEnd() 

def quads_strip(): 
    """ A linked strip of four-sided polygons. """ 
    glBegin(GL_QUAD_STRIP) 
    glColor(1.0, 0.20, 0.0)  # Dark Orange 
    vertex_set() 
    glEnd() 

def polygon(): 
    
    glBegin(GL_POLYGON) 
    glColor(1.0, 1.0, 0)  # Yellow 
    ############vertex_set()  # Unexpected Behavior
    vertex_set_polygon()
    glEnd() 

def points():
    """ Each vertex defines a point. """ 
    glPointSize( 10.0 ) 
    glBegin(GL_POINTS) 
    glColor(1.0, 0.0, 1.0)  # Purple 
    vertex_set()
    #vertex_set_polygon()
    glEnd() 

def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """ 
        glClearColor(0.0, 0.0, 0.0, 0.0)  
        #glClearColor(1.0, 0.0, 0.0, 0.0)   # try this 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() # default value of GL_PROJECTION matrix
        gluPerspective(45.0, Width/Height, 0.1, 100.0) # (note: znear can equal 0)
        
        glMatrixMode(GL_MODELVIEW) 
        glLoadIdentity() # default value of GL_MODELVIEW matrix

def DrawGLScene(): 
        """ Test each primitive. For each primitive to be tested,
            un-comment the relevant line. 
            Ensure all the others are commented out to keep the situation simple. 
        """ 
        glClear(GL_COLOR_BUFFER_BIT) 
        
        glTranslate(0.0,0.0,-3.0)
        #glTranslate(0.0,0.0,-10.0) # try this

        glLineWidth(10.0) 
        # Test the primitives. Uncomment each line by itself to demonstrate it. 
        # =====================================================
        points() 
        #unjoined_line()
        #joined_line()
        #line_loop()
        #triangles()
        #triangle_strip()
        #triangle_fan()
        #quads()
        #quads_strip() # Note the vertices order in lecture 5, slide 17
        polygon()
        
        glFlush() 
 
 
def main(): 
        """ Main Program. 
        """    
        glutInit() 
        glutInitWindowSize(600,600)    # W,H of the window. 

        glutInitWindowPosition(30,30) # Controls where the window starts - top-left corner. 
        glutCreateWindow(b'OpenGL Primitives: GL_POINTS') 
 
        glutDisplayFunc(DrawGLScene)    # The actual 'draw now' command. 
        InitGL(640, 480) 
        glutMainLoop() # starting to draw the scene

main()
