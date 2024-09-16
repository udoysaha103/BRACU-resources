from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH  = 500
WINDOW_HEIGHT = 750

class AABB:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
    
    def collides_with(self, other):
        return (self.x < other.x + other.w and # x_min_1 < x_max_2
                self.x + self.w > other.x  and # x_max_1 > m_min_2
                self.y < other.y + other.h and # y_min_1 < y_max_2
                self.y + self.h > other.y)     # y_max_1 > y_min_2

# Global variables
box1 = AABB(100, 250, 50, 50)
box2 = AABB(350, 250, 50, 50)
box_speed = 5
collision = False

def draw_box(box):
    # should draw using midpoint line algorithm
    global collision
    
    if collision:
        glColor3f(1.0, 0.0, 0.0)
    else:
        glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_POINTS)
    # bottom line
    drawline(box.x, box.y, box.x + box.w, box.y)

    # right line
    drawline(box.x + box.w, box.y, box.x + box.w, box.y + box.h)

    # top line
    drawline(box.x + box.w, box.y + box.h, box.x, box.y + box.h)

    # left line
    drawline(box.x, box.y + box.h, box.x, box.y)
    glEnd()

def draw_points(x, y, zone):
    if zone == 0:
        glVertex2f(x, y)
    elif zone == 1:
        glVertex2f(y, x)
    elif zone == 2:
        glVertex2f(-y, x)
    elif zone == 3:
        glVertex2f(-x, y)
    elif zone == 4:
        glVertex2f(-x, -y)
    elif zone == 5:
        glVertex2f(-y, -x)
    elif zone == 6:
        glVertex2f(y, -x)
    elif zone == 7:
        glVertex2f(x, -y)

def midpoint_line(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1
    d = 2*dy - dx
    dE = 2*dy
    dNE = 2*(dy - dx)
    x = x1
    y = y1
    draw_points(x, y, zone)
    while x < x2:
        if d <= 0:
            d = d + dE
            x = x + 1
        else:
            d = d + dNE
            x = x + 1
            y = y + 1
        draw_points(x, y, zone)
    return x1, y1, x2, y2

def convert_to_zone0(x1, y1, x2, y2, zone):
    if zone == 0:
        return x1, y1, x2, y2
    elif zone == 1:
        return y1, x1, y2, x2
    elif zone == 2:
        return y1, -x1, y2, -x2
    elif zone == 3:
        return -x1, y1, -x2, y2
    elif zone == 4:
        return -x1, -y1, -x2, -y2
    elif zone == 5:
        return -y1, -x1, -y2, -x2
    elif zone == 6:
        return -y1, x1, -y2, x2
    elif zone == 7:
        return x1, -y1, x2, -y2

def convert_from_zone0(x1, y1, zone):
    if zone == 0:
        return x1, y1
    elif zone == 1:
        return y1, x1
    elif zone == 2:
        return -y1, x1
    elif zone == 3:
        return -x1, y1
    elif zone == 4:
        return -x1, -y1
    elif zone == 5:
        return -y1, -x1
    elif zone == 6:
        return y1, -x1
    elif zone == 7:
        return x1, -y1

def check_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        if dx > 0:
            if dy >= 0:
                return 0
            else:
                return 7
        else:
            if dy >= 0:
                return 3
            else:
                return 4
    else:
        if dx > 0:
            if dy >= 0:
                return 1
            else:
                return 6
        else:
            if dy >= 0:
                return 2
            else:
                return 5

def drawline(x1, y1, x2, y2):
    zone = check_zone(x1, y1, x2, y2)

    x1, y1, x2, y2 = convert_to_zone0(x1, y1, x2, y2, zone)
    midpoint_line(x1, y1, x2, y2, zone)

def initialize():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def check_collision():
    global collision

    if box1.collides_with(box2):
        collision = True
    else:
        collision = False

def show_screen():
    # this function should contain the logic for drawing objects
    # DO NOT do game logic here (e.g. object movement, collision detection, sink detection etc.)

    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # draw stuffs here
    draw_box(box1)
    draw_box(box2)

    # do not forget to call glutSwapBuffers() at the end of the function
    glutSwapBuffers()

def keyboard_ordinary_keys(key, _, __):
    # check against alphanumeric keys here (e.g. A..Z, 0..9, spacebar, punctuations)
    # must cast characters to binary when comparing (e.g. key == b'q')

    glutPostRedisplay()

def keyboard_special_keys(key, _, __):
    # check against special keys here (e.g. F1..F11, arrow keys, etc.)
    # use GLUT_KEY_* constants while comparing (e.g. GLUT_KEY_F1, GLUT_KEY_LEFT, etc.)
    global box1

    if key == GLUT_KEY_UP:
        box1.y += box_speed
    elif key == GLUT_KEY_DOWN:
        box1.y -= box_speed
    elif key == GLUT_KEY_LEFT:
        box1.x -= box_speed
    elif key == GLUT_KEY_RIGHT:
        box1.x += box_speed

    glutPostRedisplay()

def mouse_click(button, state, x, y):
    # check for mouse clicks here (left, middle and right click)
    # use GLUT_LEFT_BUTTON, GLUT_MIDDLE_BUTTON, GLUT_RIGHT_BUTTON constants while comparing
    # use GLUT_DOWN and GLUT_UP constants while comparing for button state
    # You should either listen to GLUT_DOWN or GLUT_UP, so filter that out

    # convert coordinates, (flip the y-axis first)
    mx, my = x, WINDOW_HEIGHT - y

    # do your click detection here using button, state, mx, my


    glutPostRedisplay()

def animation():
    # write codes here that's going to run every frame
    # for example, updating coordinates of objects that move spotaneously
    # or collision detection, or sink detection, etc.
    # Note: DO NOT write drawing codes here

    check_collision()


    # don't forget to call glutPostRedisplay()
    # otherwise your animation will be stuck
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL AABB Collision")

glutDisplayFunc(show_screen)
glutIdleFunc(animation)

glutKeyboardFunc(keyboard_ordinary_keys)
glutSpecialFunc(keyboard_special_keys)
glutMouseFunc(mouse_click)

glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()