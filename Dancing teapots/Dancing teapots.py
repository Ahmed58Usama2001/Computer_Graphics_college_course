from mimetypes import init
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



time_interval=1
roteteinplace=0
ang=0
rotate=0
up=[1,1,1,1,0]
ytranslate=[.8,1.4,2,2.6,3]

def init():

    glMatrixMode(GL_PROJECTION)
    gluPerspective(70, 1, .1, 30)
   
    glMatrixMode(GL_MODELVIEW)

    gluLookAt(0, 5,9,
              0, 0, 0,
              0, 1, 0)

    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)

def Timer(v): 
	Display() 
	glutTimerFunc(time_interval,Timer,1)




def Display():
    global roteteinplace,ang,teapotsytrans,rotate,up,ytranslate
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glColor(1,1,1,1)
    
    glPushMatrix()
    glRotate(90,1,0,0)
    glutSolidCylinder(7, 1, 50, 20)
    glPopMatrix()
   
    ang=0
    glColor(0,1,1,1)

    for i in range(5):
        glPushMatrix()

        glRotate(rotate,0,1,0)

        if up[i]==1:
            ytranslate[i]+=.003
            if ytranslate[i]>=3:
                up[i]=0
            
        
        elif up[i]==0:
            ytranslate[i]-=.003
            if ytranslate[i]<=.8:
                up[i]=1


        glTranslate(0,ytranslate[i],0)
        
        glRotate(ang,0,1,0)

        glTranslate(5,0,0)

        glRotate(roteteinplace,0,1,0)
        glutWireTeapot(1)

        glRotate(90,1,0,0)
        glutSolidCylinder(.1, 3, 10, 5)

        ang+=72

        glPopMatrix()

        
    roteteinplace+=.1
    rotate+=.13
    
    glutSwapBuffers()


glutInit()
glutInitWindowSize(800, 700)  
glutInitWindowPosition(0, 0)  
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH)  
glutCreateWindow(b"Dancing teapots")  
init()
glutDisplayFunc(Display)  
glutTimerFunc(time_interval,Timer,1)
glutMainLoop()