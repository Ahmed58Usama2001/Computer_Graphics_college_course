from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

from solar_00 import TIMER_INTERVAL_MS, \
    planets, \
    WINDOW_WIDTH, \
    WINDOW_HEIGHT, \
    timer, \
    reposition_camera, \
    init, draw_sun, draw_planet

"""
Lighting Recipe
1) glEnable(GL_LIGHTING)
2) glEnable(GL_LIGHT0)
3) set light characteristics
    glLight(GL_LIGHT0, GL_POSITION, LightPos)
    glLight(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLight(GL_LIGHT0, GL_DIFFUSE, LightDif)
    glLight(GL_LIGHT0, GL_SPECULAR, LightSpc)

4) set material of a model (this replaces glColor(r, g, b) commands)
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT, MaterialAmb)
    glMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE, MaterialDif)
    glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, MaterialSpc)
    glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, MaterialShn)

NOTE: the minimum value is -1 not 0
"""


def new_init():
    init()
    glEnable(GL_LIGHTING)  # >>>>>>>>>>>>> step 1


def enableLight0():
    glEnable(GL_LIGHT0)  # >>>>>>>>>>>>> step 2

    LightPos = [0.0, 0.0, 0.0, 1.0]  # x,y,z, w [0: Infinite(directional), 1: positional] # TODO set w = 0
    LightAmb = [0.3, 0.3, 0.0, 1.0]  # r,g,b, alpha
    LightDif = [1.0, 1.0, 0.0, 1.0]
    LightSpc = [1.0, 1.0, 1.0, 1.0]  # white

    # step 3
    glLight(GL_LIGHT0, GL_POSITION, LightPos)
    glLight(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLight(GL_LIGHT0, GL_DIFFUSE, LightDif)
    glLight(GL_LIGHT0, GL_SPECULAR, LightSpc)


def draw_sun_with_light():
    glTranslate(0, 0, 0)

    #################################################
    # this replaces glColor(1.0, 1.0, 0.0)  # yellow
    MaterialAmb = [1.0, 1.0, 0.0, 1.0]  # YELLOW LIGHT FROM SUN
    MaterialDif = [1.0, 1.0, 0.0, 1.0]  # YELLOW LIGHT FROM SUN
    MaterialSpc = [1.0, 1.0, 1.0, 1.0]  #
    MaterialShn = [16]  # 0-128
    glMaterial(GL_FRONT, GL_AMBIENT, MaterialAmb)
    glMaterial(GL_FRONT, GL_DIFFUSE, MaterialDif)
    glMaterial(GL_FRONT, GL_SPECULAR, MaterialSpc)
    glMaterial(GL_FRONT, GL_SHININESS, MaterialShn)
    #################################################
    glutSolidSphere(1.5, 30, 30)


def draw_planet_with_light(sun_dist, radius, r, g, b, angular_position=0):
    # angular_position in degrees
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    # Orbit
    ##########################################
    # those following commands replace glColor(1, 1, 1)
    MaterialAmb = [1.0, 1.0, 0.0, 1.0]  # r,g,b, alpha
    MaterialDif = [0.00, 0.00, 0.0, 1.0]
    MaterialSpc = [0.0, 0.0, 0.0, 1.0]
    MaterialShn = [128]  # 0-128

    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT, MaterialAmb)  # step 4
    glMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE, MaterialDif)  # step 4
    glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, MaterialSpc)  # step 4
    glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, MaterialShn)  # step 4
    ##########################################
    glutSolidTorus(0.03, sun_dist, 10, 50)

    # Planet
    # those following commands replace glColor(r, g, b)
    MaterialAmb = [r, g, b, 1]  # r,g,b, alpha
    MaterialDif = [r, g, b, 1]
    MaterialSpc = [r, g, b, 1]
    MaterialShn = [128]  # 0-128

    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT, MaterialAmb)  # step 4
    glMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE, MaterialDif)  # step 4
    glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, MaterialSpc)  # step 4
    glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, MaterialShn)  # step 4
    #######################
    glRotate(angular_position, 0, 0, 1)
    glTranslate(sun_dist,
                0,
                0)
    #######################
    # glTranslate(sun_dist * cos(angular_position * pi / 180),
    #             sun_dist * sin(angular_position * pi / 180),
    #             0)
    #######################
    glutSolidSphere(radius, 30, 30)
    glPopAttrib()
    glPopMatrix()


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    reposition_camera()
    # sun
    draw_sun_with_light()

    # 8 planets
    for planet_name in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        planet = planets[planet_name]
        draw_planet_with_light(planet["sun_dist"],
                               planet["radius"],
                               planet["R"],
                               planet["G"],
                               planet["B"],
                               planet["angular_position"])

        planet["angular_position"] = (planet["angular_position"] % 360) + planet["velocity"]  # make a step

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Solar System-lighting")
    glutDisplayFunc(draw)
    glutTimerFunc(TIMER_INTERVAL_MS, timer, 1)
    new_init()
    enableLight0()  # NEW: enable lighting
    glutMainLoop()


if __name__ == "__main__":
    main()
