from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from lecture_00 import init, \
    WINDOW_WIDTH, \
    WINDOW_HEIGHT, \
    FROM_RIGHT, \
    FROM_LEFT, \
    FROM_TOP, \
    FROM_BOTTOM, \
    INTERVAL, \
    Rectangle, \
    keyboard_callback, \
    draw_text, \
    check_ball_wall, \
    draw_rectangle

####################################
########### game state #############
####################################
current_delta_X = 1
current_delta_y = 1

current_ball = Rectangle(140, 140, 160, 160)  # initial rect of the ball # TODO: try different numbers
current_wall = Rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
current_player1 = Rectangle(0, 0, 140, 20)  # initial rect of player1 bat # TODO: try different numbers
current_player2 = Rectangle(0, WINDOW_HEIGHT - 20, 140, WINDOW_HEIGHT)  # initial rect of player2 bat # TODO: try different numbers

current_player1_result = 0
current_player2_result = 0

current_mouse_x = 0
current_keyboard_x = 0

current_color_anim = 1


####################################

def check_ball_player1(_ball, _player1):
    # Collision Detection between Ball and player1's bat
    # check  sheet 5)b), the ball should bounce if there's ANY overlap (ball's left OR right)
    # _ball and _player1 can be replaced by the global states

    left_overlap = _player1.left <= _ball.left <= _player1.right
    right_overlap = _player1.left <= _ball.right <= _player1.right
    horizontal_overlap = (left_overlap or right_overlap)
    vertical_check = _ball.bottom <= _player1.top
    is_going_down = current_delta_y == -1  # TODO: set is_going_down = True and you can hack the game :3, tell me how
    return vertical_check and horizontal_overlap and is_going_down


def check_ball_player2(_ball, _player2):
    # Collision Detection between Ball and player2's bat
    # check  sheet 5)b), the ball should bounce if there's ANY overlap (ball's left OR right)
    # _ball and _player2 can be replaced by the global states

    left_overlap = _player2.left <= _ball.left <= _player2.right
    right_overlap = _player2.left <= _ball.right <= _player2.right
    horizontal_overlap = (left_overlap or right_overlap)

    vertical_check = _ball.top >= _player2.bottom
    is_going_up = current_delta_y == 1  # TODO: set is_going_down = True and you can hack the game :3, tell me how
    return vertical_check and horizontal_overlap and is_going_up


####################################
############# callbacks  ###########
####################################

def mouse_player1_callback(x, y):
    global current_mouse_x
    current_mouse_x = x  # we only track the x coordinate


def keyboard_player2_callback(key, x, y):
    global current_keyboard_x
    if key == GLUT_KEY_LEFT:
        current_keyboard_x = max(current_keyboard_x - 10, 0)
    elif key == GLUT_KEY_RIGHT:
        current_keyboard_x = min(current_keyboard_x + 10, WINDOW_WIDTH)


####################################
############# timers  ##############
####################################

def game_timer_section(v):
    # a new timer
    display_section()  # this is the only difference
    print(v)
    glutTimerFunc(INTERVAL, game_timer_section, 1)  # TODO: replace 1 by v+1


########################################################
def display_section():
    global current_delta_X
    global current_delta_y

    global current_player2_result
    global current_player1_result
    global current_color_anim

    glClear(GL_COLOR_BUFFER_BIT)

    string = "Player1: " + str(current_player1_result)
    draw_text(string, 10, 440)
    string = "Player2: " + str(current_player2_result)
    draw_text(string, 10, 400)

    current_ball.left = current_ball.left + current_delta_X  # updating ball's coordinates
    current_ball.right = current_ball.right + current_delta_X
    current_ball.top = current_ball.top + current_delta_y
    current_ball.bottom = current_ball.bottom + current_delta_y

    glColor(0, 1, 1)  # White color

    draw_rectangle(current_ball)

    glColor(1, current_color_anim, current_color_anim)  # red when current_color_anim = 0, white when current_color_anim = 1

    # print(Test_Ball_Wall(ball,wall))

    if check_ball_wall(current_ball, current_wall) == FROM_RIGHT:
        current_delta_X = -1

    if check_ball_wall(current_ball, current_wall) == FROM_LEFT:
        current_delta_X = 1

    if check_ball_wall(current_ball, current_wall) == FROM_TOP:
        current_delta_y = -1
        current_player1_result = current_player1_result + 1

    if check_ball_wall(current_ball, current_wall) == FROM_BOTTOM:
        current_delta_y = 1
        current_player2_result = current_player2_result + 1

    current_player1.left = current_mouse_x - 70
    current_player1.right = current_mouse_x + 70
    draw_rectangle(current_player1)

    current_player2.left = current_keyboard_x - 70
    current_player2.right = current_keyboard_x + 70
    draw_rectangle(current_player2)

    if check_ball_player1(current_ball, current_player1):  # returns true if the ball hits player1's bat
        current_delta_y = 1
        current_color_anim = 0
        current_player1_result = current_player1_result + 1

    if check_ball_player2(current_ball, current_player2):  # returns true if the ball hits player2's bat
        current_delta_y = -1
        current_color_anim = 0
        current_player2_result = current_player2_result + 1

    if current_color_anim < 1:
        current_color_anim += 0.01

    glutSwapBuffers()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Simple Ball Bat OpenGL game")
    glutDisplayFunc(display_section)
    glutTimerFunc(INTERVAL, game_timer_section, 1)
    glutKeyboardFunc(keyboard_callback)
    glutSpecialFunc(keyboard_player2_callback)  # newly added, to track keyboard events
    glutPassiveMotionFunc(mouse_player1_callback)  # TODO: can we replace this with mouse_callback from lecture code?
    init()
    glutMainLoop()
