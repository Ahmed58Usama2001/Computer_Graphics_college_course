
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# globals for animation, ball position
# and direction of motion
global anim, x, y ,dir_x, dir_y

# initial position of the center of the ball.
x = .86
y = -0.43
radius = 0.1 # Ball's Raduis

# Direction "sign" of the ball's motion
dir_x = dir_y = 1

# Window dimensions
width = height = 600
axrng = 1

# No animation to start
anim = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Make axrng larger and see what happens!-->the size of the ball reduced!!
    glOrtho(-axrng, axrng, -axrng, axrng, -axrng, axrng)
    #gluPerspective(80,1,0.01,100) # try this
    
    glMatrixMode(GL_MODELVIEW)
    

    

def bounce():
    global x, y, dir_x, dir_y
    
    glColor(1,0,0)
    glClear(GL_COLOR_BUFFER_BIT) # try comment this line

    if anim == 1:
        # changes x and y
        x = x + dir_x*0.001
        y = y + dir_y*0.001

        # Collision detection!
        # What happens here and why does this work?
        # Collision response can be even more complicated if we want the physics to be accurate!
        
        if x > axrng or x < -axrng: # The bouncing ball is sinking into the walls
        #if x > axrng-radius or x < -axrng+radius: # changing its direction when (the outer border hits a wall)
            #print("x=",x)
            dir_x = -dir_x  # actually changing its direction when the center point hits a wall (not when the outer border hits a wall)


        if y > axrng or y < -axrng: # The bouncing ball is sinking into the walls
        #if y > axrng-radius or y < -axrng+radius: # changing its direction when (the outer border hits a wall)
            #print("y=",y)
            dir_y = -dir_y  # actually changing its direction when the center point hits a wall (not when the outer border hits a wall)
        
    # Keep the motion mathematics
    # Move the ball location based on x and y
    glLoadIdentity()
    glTranslate(x,y,-1)
 #   glTranslate(x,y,-1.1) # try this-->outside the cuboid nothing will appear
    #glTranslate(.5,.5,-1) #fixed image-->we didn`t use the variables x and y
    glutSolidSphere(radius, 50, 50)
        

    glutSwapBuffers()

    
def keyboard(key1, x, y):
    # Allows us to quit by pressing 'q'
    # We can animate by "a" and stop by "s"
    #x and y are the coordinates of the mouse but we didn`t use it here`
    global anim
    
    if key1 == b"a":
        # Notice we are making anim = 1
        # What does this mean? Look at the idle function
        anim = 1
    if key1 == b"s":
        # STOP the ball!
        anim = 0
    if key1 == b"q":
        sys.exit()
        
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
    glutInitWindowPosition(100,100)
    glutInitWindowSize(width,height)
    glutCreateWindow(b"PyBounce0")
    glutDisplayFunc(bounce)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(bounce)
    init()
    glutMainLoop()
    
main()
