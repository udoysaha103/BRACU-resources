from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500,500
ball_size = 6
points = []
paused = False
blink = False
time_count = 0


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)


def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b


def keyboardListener(key, x, y):
    global paused
    if key==b' ':
        if paused:
            paused = False
        else:
            paused = True

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    if key==GLUT_KEY_UP and not paused:
        for p in points:
            if p.dx < 50:
                p.dx += 0.1
                p.dy += 0.1
    elif key== GLUT_KEY_DOWN and not paused:
        for p in points:
            if p.dx > 0:
                p.dy -= 0.1
                p.dx -= 0.1
    
    glutPostRedisplay()


def mouseListener(button, state, x, y):
    global blink

    if button==GLUT_LEFT_BUTTON and state == GLUT_DOWN and not paused:
        if blink:
            blink = False
        else:
            blink = True
        
    if button==GLUT_RIGHT_BUTTON and state == GLUT_DOWN and not paused:
        a, b = convert_coordinate(x,y)

        for p in range(random.randint(2, 20)):
            points.append(Point(a, b))

        glutPostRedisplay()

    glutPostRedisplay()


def display():
    global time_count
     #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    # main works are called here
    glPointSize(ball_size)
    glBegin(GL_POINTS)
    for p in points:
        if blink:
            if time_count < 2000:
                glColor3f(0,0,0)
            elif time_count < 4000:
                glColor3f(p.color[0], p.color[1], p.color[2])
            else:
                time_count = -1
            
            time_count += 1
        else:
            glColor3f(p.color[0], p.color[1], p.color[2])
        glVertex2f(p.x, p.y)
    glEnd()
    
    glutSwapBuffers()


def animate():
    if not paused:
        glutPostRedisplay()
        for p in points:
            p.x += p.dx
            p.y += p.dy

            if p.x > W_Width/2 or p.x < -W_Width/2:
                p.dx *= -1
            if p.y > W_Height/2 or p.y < -W_Height/2:
                p.dy *= -1


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
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

wind = glutCreateWindow(b"Assignment problem 2")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL
