from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Constants
window_width = 800
window_height = 600
points = []

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    
    # Draw points
    glBegin(GL_POINTS)
    for x, y, dx, dy, r, g, b in points:
        glColor3f(r, g, b)
        glVertex2f(x, y)
    glEnd()
    
    glFlush()

def generate_random_points(x, y, num_points):
    new_points = []
    for _ in range(num_points):
        dx, dy = random.uniform(-1, 1), random.uniform(-1, 1)
        r, g, b = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
        new_points.append((x, y, dx, dy, r, g, b))
    return new_points

def right_click(x, y, button, state):
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        new_points = generate_random_points(x, window_height - y, num_points=5)
        points.extend(new_points)
        glutPostRedisplay()

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)	#display callback function
glutMouseFunc(right_click)

glutMainLoop()		#The main loop of OpenGL