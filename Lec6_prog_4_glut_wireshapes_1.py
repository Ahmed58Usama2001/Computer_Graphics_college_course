""" Lec6 prog.4  
Program name: glut_wireshapes_1.py 
Objective: Draw all the GLUT predefined shapes. 

keywords: opengl, cube, hexagon, teapot, cone, platonics, extrusion shapes. 
==============================================================================79 

Author:  De Fine 
===============================
"""


from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 

# Rotation angle for the shapes. 
rangle = 0.0 #WHY global variable

 
def InitGL(Width, Height):                    
    """ Initialize our OpenGL window. Sets all of the initial parameters. 
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)             # Set the background to black
    glEnable(GL_DEPTH_TEST) # try to comment this and notice teapot and blue Cone

    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                                             
    gluPerspective(45.0, Width/Height, 0.1, 300.0)  # change zfar and notice when the models disapper 

    glMatrixMode(GL_MODELVIEW)
    
    
#===================================================================== 
# Initial position of the four groups 
location_1 = [2.0, 0.0, -5.0] 
location_2 = [-1.0, 0.0, -1.0] 
location_3 = [4.0, 0.0, -4.0] 
location_4 = [-2.0, 0.0, -2.0] 


def DrawGLScene(): 
  """ The drawing function 
  """ 
  global rangle  # Angular rotation 
  global location_1, location_2, location_3, location_4 

  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the Screen and the Depth Buffer. 
  rot_axis = [ 0.0, 1.0, 1.0 ] 
 
  '''  
  # Draw a cube, Icosahedron and torus 
  glLoadIdentity() # necessary to remove the previous transformations
  location_1[1] = location_1[1] + 0.01
  location_1[2] = location_1[2] - 0.05
  #glTranslate(0, 0, -250.0) # try this
  glTranslate(location_1[0], location_1[1], location_1[2]) 
  glRotate(rangle , rot_axis[0], rot_axis[1], rot_axis[2] )
  glColor(1,1,0)
  #glutSolidCube(2.5) # try this
  glutSolidIcosahedron() # try this
  glutSolidTorus(0.4, 4.4, 12, 8) 
  
      
  # Draw octahedron and sphere. 
  glLoadIdentity() # necessary to remove the previous transformations
  location_2[0] = location_2[0] + 0.01 
  location_2[2] = location_2[2] - 0.03 
  glTranslate(location_2[0], location_2[1], location_2[2]) 
  glRotate(rangle , rot_axis[0], rot_axis[1], rot_axis[2] )
  glColor(1,0,0)
  #glutWireOctahedron() # try this
  #glutWireSphere(0.75, 40, 30) # try this
  glutSolidOctahedron() 
  glutSolidSphere(0.75, 40, 30) 
  ''' 
  
  # Draw cone and dodecahedron 
  glLoadIdentity() # necessary to remove the previous transformations
  location_3[0] = location_3[0] - 0.001 
  location_3[2] = location_3[2] - 0.01 
  glTranslate(location_3[0], location_3[1], location_3[2]) 
  glRotate(rangle , rot_axis[0], rot_axis[1], rot_axis[2] )
  glColor(0,0,1)
  #glutWireCone(2.5, 2.0, 6, 6) # try this
  #glutWireDodecahedron()  # try this
  glutSolidCone(2.5, 5.0, 20, 20) 
  glutSolidDodecahedron() 

    
  # Draw Teapot 
  glLoadIdentity() # necessary to remove the previous transformations
  location_4[0] = location_4[0] + 0.01 
  location_4[2] = location_4[2] - 0.05 
  glTranslate(location_4[0], location_4[1], location_4[2]) 
  glRotate(rangle , rot_axis[0], rot_axis[1], rot_axis[2] )
  glColor(0,1,1)
  #glutWireTeapot(1.5) # try this
  glutSolidTeapot(1.5) 
  
    
  rangle = rangle + 0.5 
  glutSwapBuffers() 

def main(): 
  """ Main Program. 
  """     
  glutInit() # initialization openGL window. Must be first GLUT function called. 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   # Display mode 
  glutInitWindowSize(800, 800) 
  glutInitWindowPosition(0, 0)  
  glutCreateWindow(b"GLUT Wireshapes") 
  glutDisplayFunc(DrawGLScene) 
  glutIdleFunc(DrawGLScene)  # When we are doing nothing, redraw the scene. No animation without this. 
  InitGL(800, 800)                # Call our custom initialization function. 
  glutMainLoop()                  # Start GLUT's Event Processing Engine  

main()
