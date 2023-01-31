from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init_projection():
    # invoked only once at the beginning
    glMatrixMode(GL_PROJECTION)
    gluPerspective(20, 1, 1, 30)
    glMatrixMode(GL_MODELVIEW)


def draw_axes():
    # # z(blue) >>> left - right
    # # y(green) >>> top - bottom
    # # x(red) >>> front - back

    glBegin(GL_LINES)
    # X axis
    glColor3f(1, 0, 0)  # red
    glVertex3d(0, 0, 0)
    glVertex3d(100, 0, 0)

    # Y axis
    glColor3f(0, 1, 0)  # green
    glVertex3d(0, 0, 0)
    glVertex3d(0, 100, 0)

    # Z axis
    glColor3f(0, 0, 1)  # blue
    glVertex3d(0, 0, 0)
    glVertex3d(0, 0, 100)

    glEnd()


def reposition_camera():
    # NOTE: this code operates on modelview matrix
    #######################################
    # camera 1
    #####################
    # position the camera
    gluLookAt(0, 0, 15,  # eye # TODO change 15 to 50, or 20 what do you see?
             0, 0, 0,  # center
            0, 1, 0)  # up vector
    #######################################
    # camera 2
    #####################
     # TODO try this: like a cube -->here we will see z axis as we look at it from up veiw not looking at it as a point in the same veiw
    # gluLookAt(10, 10, 10,  # eye
   #            0, 0, 0,  # center
    #          0, 1, 0)  # up vector
    #######################################


def draw():
    # clear
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    # # #########################################
    # AXES
    glLoadIdentity() #--> optional as there is no last effects to delete
    reposition_camera() #--> mandatory to look at the drawn axis from right place
    draw_axes()
    # # #########################################
    # # ######## bottom cube
    glColor3f(1, 0, 0)  # red
    glLoadIdentity() #Mandatory to delete the effect of transformations on last thing drawn
    reposition_camera()  # TODO try to comment this-->this cube will not be seen as the (load identity) will delete the model veiw matrix including the veiw of the camera
    glTranslate(0, 0, 0)
    glScale(4, 1, 2)
    glutWireCube(1)
    # # # #########################################
    # # ########## top cube
    glLoadIdentity()
    reposition_camera()
    glTranslate(0, .5 + .35, 0)  # .5 = height of the bottom cube, .35 is = height of the top cube..half of scaled .7
    glScale(2, .7, 1.5)

    glutWireCube(1)
    # # # #########################################
    # # # ############# wheels
    glColor3f(0, 0, 1)
    # the bottom cube is scaled (4*X, 1*Y, 2*Z)
    # z(blue) >>> left - right
    # y(green) >>> top - bottom
    # x(red) >>> front - back
    draw_wheel(loc_x=+2, loc_y=-0.5, loc_z=-1)  # left front wheels
    draw_wheel(loc_x=-2, loc_y=-0.5, loc_z=-1)  # left rear wheels
    draw_wheel(loc_x=+2, loc_y=-0.5, loc_z=1)  # right front wheels
    draw_wheel(loc_x=-2, loc_y=-0.5, loc_z=1)  # right rear wheels
    # # # #########################################
    # # # ############# headlight bulbs
    glColor3f(1, 1, 0)
    draw_headlight_bulb(loc_x=+2, loc_y=0, loc_z=-.5)  # left bulb
    draw_headlight_bulb(loc_x=+2, loc_y=0, loc_z=+.5)  # right bulb
    # # # #########################################
    glFlush()


def draw_wheel(loc_x, loc_y, loc_z):
    glLoadIdentity()
    reposition_camera()
    glTranslate(loc_x, loc_y, loc_z)
    glutWireTorus(0.15, 0.35, 10, 12)  # TODO: play with those


def draw_headlight_bulb(loc_x, loc_y, loc_z):
    glLoadIdentity()
    reposition_camera()
    glTranslate(loc_x, loc_y, loc_z)
    glScale(.2, 3, 3)
    glutWireSphere(0.1, 20, 20)


if __name__ == "__main__":  # TODO try to remove this?
    glutInit()
  #  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Moving Car")
    glutPositionWindow(500, 160)
    init_projection()
    glutDisplayFunc(draw)
    glutMainLoop()
