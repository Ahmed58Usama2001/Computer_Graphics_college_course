"""
    Lec8 prog.1  
""" 

from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
from math import *

PI = 22/7
rangle = 0


def keyboard(key,x,y):
    global LightPos
    if key == b"a":
        LightPos[0] = LightPos[0] - 0.2
    if key == b"s":
        LightPos[0] = LightPos[0] + 0.2
    if key == b"d":
        LightPos[1] = LightPos[1] - 0.2
    if key == b"f":
        LightPos[1] = LightPos[1] + 0.2
    if key == b"g":
        LightPos[2] = LightPos[2] - 0.2
    if key == b"h":
        LightPos[2] = LightPos[2] + 0.2
    if key == b"r":
        LightPos[0] = 0
        LightPos[1] = 0
        LightPos[2] = 3

    print(LightPos[0],",",LightPos[1],",",LightPos[2],"\n")

    
##################################################################################################

#LightPos     =  [ 0, 0 , -3 , 0 ]  # Directional light source is at infinite, z = -infinte
#LightPos     =  [ 0, 0 , 3 , 0 ]   # Directional light source is at infinite, z = +infinte
#LightPos     =  [ 0, 3 , 0 , 0 ]   # Directional light source is at infinite, y = +infinte
    
LightPos     =  [ 0, 0 , 3 , 1 ] # Positional light source
LightAmb     =  [ 1, 1 , 1 , 1.0 ]   # RGBA of Ambient Light
LightDiff    =  [ 1, 1 , 1 , 1.0 ]  # RGBA of Diffuse Light
LightSpec    =  [ 0, 1 , 0 , 1.0 ]  # RGBA of Specular Light


##################################################################################

# Relection of front-face Material
#MatAmbF       =  [ 0 , 0 , 0 ,1 ] # try this
MatAmbF       =  [ 0.0 , 0.4 , 0 ,1 ]
MatDifF       =  [ 1 , 0 , 0 ,1 ]
MatSpecF      =  [ 1 , 1 , 1 ,1 ] # The color of the highlight will be yellow = (Red from Diffuse + Green from Specular)
#MatSpecF      =  [ 0 , 0 , 0 ,0 ]  # try this
MatShnF       =  [ 128 ]


#####################################################################################

# Relection of back-face Material
MatAmbB       =  [ 0 , 0 , 0.4 ,1 ]
MatDifB       =  [ 0 , 0 , 1 ,1 ]
MatSpecB      =  [ 1 , 1 , 1 ,1 ]
MatShnB       =  [ 128 ]



def InitGL(Width, Height):        
    
    glClearColor(1.0, 1.0, 1.0, 0.0)

        
# ^^^^^^^^^^^^ Lighting and Materials ^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        
    glLightfv(GL_LIGHT0, GL_POSITION, LightPos) 
    glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  LightDiff)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LightSpec) 

    
    glEnable(GL_LIGHTING) # After enabling the lighting, "glColor" has no effect. If you comment this line, you will see the effect of "glColor"
    glEnable(GL_LIGHT0)


    # turn on two-sided (Front & Back faces) lighting
    # When we turn on two-sided lighting: 1) use the GL_BACK (or GL FRONT AND BACK) parameter values to color backfacing polygons, and 2) (b) reverse the specified vertex normal (-Normal vector) for back-facing polygons [Back face is let by ambient light and diffuse light].
    # When we turn off two-sided lighting: 1) use the GL_FRONT parameter values to color backfacing polygons, and 2) (b) the specified vertex normal (Normal vector) for back-facing polygons[Back face is let only by ambient light].
    
    glLightModeli( GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE ) # try to comment this  
    
    
    glMaterialfv(GL_FRONT, GL_AMBIENT , MatAmbF)
    glMaterialfv(GL_FRONT, GL_DIFFUSE , MatDifF)
    glMaterialfv(GL_FRONT, GL_SPECULAR , MatSpecF)
    glMaterialfv(GL_FRONT, GL_SHININESS , MatShnF)
    
    
    glMaterialfv(GL_BACK, GL_AMBIENT , MatAmbB)
    glMaterialfv(GL_BACK, GL_DIFFUSE , MatDifB)
    glMaterialfv(GL_BACK, GL_SPECULAR , MatSpecB)
    glMaterialfv(GL_BACK, GL_SHININESS , MatShnB)
        
        

    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()          
    gluPerspective(30.0, Width/Height, 0.1, 100.0)
    
    # Camera is at (0,0,5)
    gluLookAt(0,0,5 , 0,0,0 , 0,1,0)
    # Note: "gluLookAt()" must be defined after gluPerspective( )

    
    glMatrixMode(GL_MODELVIEW)
    

    
                
# The main drawing function. 
def DrawGLScene(): 
    global rangle
    
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )  # Clear The Screen and Depth buffers
       
    glLightfv(GL_LIGHT0, GL_POSITION, LightPos) # We need this line because the function "keyboard()" changes the values of "LightPos"    
        
    glColor(0,1,0)  # this green color doesn't affect the final color

###########################################################################3    
    '''
    # Model(1)
    glLoadIdentity()
    glRotate(rangle,0,1,0)
    
    # Front-Face
    glBegin(GL_QUADS)
    
    # Coordinates of the vector [0,0,1] around Y-axis (see the rotation matrix Ry in lecture 2 slide 18 , Q=Trans(Inv(Ry)= Ry )  )
    Nx = (0)*cos(rangle*PI/180) + (1)*sin(rangle*PI/180)
    Ny = 0
    Nz = (0)*-sin(rangle*PI/180) + (1)*cos(rangle*PI/180)
    glNormal(Nx,Ny,Nz)

    # default vaule of the normal vector = (0,0,1)
    #glNormal(0,0,1)  # try this
    #glNormal(0,0,-1)  # try this

    #Counter Clock-wise (CCW)
    glVertex(0.5,-0.5,0)  # v0
    glVertex(0.5,0.5,0)   # v1
    glVertex(-0.5,0.5,0)  # v2
    glVertex(-0.5,-0.5,0) # v3

    glEnd()
    '''
#########################################################################
    
    '''
    # Model(2)
    glLoadIdentity()
    glRotate(rangle,0,1,0)
    
    # Back-Face
    glBegin(GL_QUADS)    

    # Coordinates of the vector [0,0,-1] around Y-axis (see the rotation matrix Ry in lecture 2  , Trans(inv(Ry)= Ry )
    Nx = (0)*cos(rangle*PI/180) + (-1)*sin(rangle*PI/180)
    Ny = 0
    Nz = (0)*-sin(rangle*PI/180) + (-1)*cos(rangle*PI/180)
    glNormal(Nx,Ny,Nz)

    #glNormal(0,0,-1) # try this
    #glNormal(0,0,1) # try this

    #Clock-wise (CW)
    glVertex(-0.5,-0.5,0) # v3
    glVertex(-0.5,0.5,0)  # v2
    glVertex(0.5,0.5,0)   # v1
    glVertex(0.5,-0.5,0)  # v0

    glEnd()
    '''
    


    # If you disable GL_DEPTH_TEST, then the back face covers up the front face.
    glEnable(GL_DEPTH_TEST) # If you will draw the solid sphere, then try to disable GL_DEPTH_TEST and see what's happening?

    # Model(3)
    glutSolidSphere(0.5,100,100)

    rangle = rangle + 0.1 # try to comment this line
    glutSwapBuffers()
    
    

    

def main(): 
    glutInit() 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH )
    glutInitWindowSize(600, 600) 
    glutInitWindowPosition(0, 0)  
    glutCreateWindow(b"Lighting") 
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutKeyboardFunc(keyboard)
    InitGL(600, 600)                
    glutMainLoop()                 

main()
