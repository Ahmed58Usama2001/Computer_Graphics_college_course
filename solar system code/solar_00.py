from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
TIMER_INTERVAL_MS = 1  # try  2,5,7 msec

# PLANET DATA
planets = {
    "Mercury": {"angular_position": 0,
                "velocity": 0.01,
                "sun_dist": 3,
                "radius": 0.2,
                "R": 0.5,
                "G": 0.1,
                "B": 0.9},
    "Venus": {"angular_position": 0, "velocity": 0.007, "sun_dist": 5, "radius": 0.3, "R": 0.2, "G": 0.8, "B": 0.1},
    "Earth": {"angular_position": 0, "velocity": 0.008, "sun_dist": 7, "radius": 0.4, "R": 0, "G": 0, "B": 1},
    "Mars": {"angular_position": 0, "velocity": 0.011, "sun_dist": 9, "radius": 0.4, "R": 0.8, "G": 0.4, "B": 0.3},
    "Jupiter": {"angular_position": 0, "velocity": 0.012, "sun_dist": 11, "radius": 0.8, "R": 0.6, "G": 0.7, "B": 0.6},
    "Saturn": {"angular_position": 0, "velocity": 0.009, "sun_dist": 13, "radius": 0.5, "R": 0.1, "G": 0.8, "B": 0.3},
    "Uranus": {"angular_position": 0, "velocity": 0.008, "sun_dist": 15, "radius": 0.6, "R": 0.9, "G": 0.1, "B": 0.7},
    "Neptune": {"angular_position": 0, "velocity": 0.012, "sun_dist": 17, "radius": 0.2, "R": 0.4, "G": 0.3, "B": 0.0},
}


def init():
    glClearColor(0.0, 0.0, 0.0, 0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 50)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def timer(v):
    glutPostRedisplay()  # re-call draw function
    print(v)
    glutTimerFunc(TIMER_INTERVAL_MS, timer, v + 1)


def reposition_camera():
    gluLookAt(17, 17, 17,
              0, 0, 0,
              0, 0, 1)


def draw_axes():
    glLineWidth(10)
    glBegin(GL_LINES)
    # X
    glColor3f(1, 0, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(100, 0, 0)

    # Y
    glColor3f(0, 1, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 100, 0)

    # Z
    glColor3f(0, 0, 1)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 0, 100)

    glColor3f(1, 1, 1)
    glEnd()


def draw_sun():
    glTranslate(0, 0, 0)
    glColor(1.0, 1.0, 0.0)  # yellow
    glutSolidSphere(1.5, 30, 30)


def draw_planet(sun_dist, radius, r, g, b, angular_position=0):
    # angular_position in degrees
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    # Orbit
    glColor(1, 1, 1)
    glutSolidTorus(0.03, sun_dist, 10, 50)

    # Planet
    glColor(r, g, b)
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


#
# Saturn_position = 0
# Saturn_velocity = 0.9


def draw():
    # global Saturn_position
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    reposition_camera()
    draw_axes()
    draw_sun()
    # draw_planet(13, 0.5, 0.1, 0.8, 0.3, Saturn_position)
    # Saturn_position = Saturn_position + Saturn_velocity
    for planet_name in ["Saturn", "Neptune"]:
        planet = planets[planet_name]
        draw_planet(planet["sun_dist"],
                    planet["radius"],
                    planet["R"],
                    planet["G"],
                    planet["B"],
                    planet["angular_position"])

        planet["angular_position"] = planet["angular_position"] + planet["velocity"]  # make a step
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Solar System")
    glutDisplayFunc(draw)
    glutTimerFunc(TIMER_INTERVAL_MS, timer, 1)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
