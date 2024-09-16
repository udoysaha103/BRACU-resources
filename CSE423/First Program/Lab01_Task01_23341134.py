from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

W_Width, W_Height = 500,500
currentMode = "day"
dayMode_bg = (1, 1, 1)
nightMode_bg = (0, 0, 0)
currentMode_bg = dayMode_bg
currentMode_fg = nightMode_bg
displacement = 0
displacement_speed = 10
rain_x = 0
rain_start_y = 500
rain_end_y = -500
rain_speed = 0.35


def keyboardListener(key, x, y):
    global currentMode, currentMode_bg, currentMode_fg

    if key==b'n':
        if currentMode == 'day':
            time.sleep(0.2)
            currentMode_bg = nightMode_bg
            currentMode_fg = dayMode_bg
            drawHome()
            currentMode = 'night'
            print("Night")

    elif key==b'd':
        if currentMode == 'night':
            time.sleep(0.2)
            currentMode_bg = dayMode_bg
            currentMode_fg = nightMode_bg
            drawHome()
            currentMode = 'day'
            print("Day")

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global displacement, rain_x

    if key==GLUT_KEY_RIGHT:
        if displacement < 300:
            displacement += displacement_speed
            rain_x += displacement_speed
    if key== GLUT_KEY_LEFT:
        if displacement > -300:
            displacement -= displacement_speed
            rain_x -= displacement_speed
    glutPostRedisplay()

def animate():
    glutPostRedisplay()
    global rain_start_y, rain_end_y
    if rain_start_y > 300:
        rain_start_y -= rain_speed
        rain_end_y -= rain_speed
    else:
        rain_start_y = 500
        rain_end_y = -500

def drawRain():
    glColor3f(currentMode_fg[0], currentMode_fg[1], currentMode_fg[2])
    glLineWidth(3.0)  # Set line width
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(4, 0x0FFF)

    glBegin(GL_LINES)

    glVertex2f(-800+rain_x, rain_start_y)
    glVertex2f(-800+rain_x+displacement, rain_end_y)

    glVertex2f(-700+rain_x, rain_start_y)
    glVertex2f(-700+rain_x+displacement, rain_end_y)

    glVertex2f(-600+rain_x, rain_start_y)
    glVertex2f(-600+rain_x+displacement, rain_end_y)

    glVertex2f(-500+rain_x, rain_start_y)
    glVertex2f(-500+rain_x+displacement, rain_end_y)

    glVertex2f(-400+rain_x, rain_start_y)
    glVertex2f(-400+rain_x+displacement, rain_end_y)

    glVertex2f(-300+rain_x, rain_start_y)
    glVertex2f(-300+rain_x+displacement, rain_end_y)

    glVertex2f(-200+rain_x, rain_start_y)
    glVertex2f(-200+rain_x+displacement, rain_end_y)

    glVertex2f(-100+rain_x, rain_start_y)
    glVertex2f(-100+rain_x+displacement, rain_end_y)

    glVertex2f(0+rain_x, rain_start_y)
    glVertex2f(0+rain_x+displacement, rain_end_y)

    glVertex2f(100+rain_x, rain_start_y)
    glVertex2f(100+rain_x+displacement, rain_end_y)

    glVertex2f(200+rain_x, rain_start_y)
    glVertex2f(200+rain_x+displacement, rain_end_y)

    glVertex2f(300+rain_x, rain_start_y)
    glVertex2f(300+rain_x+displacement, rain_end_y)

    glVertex2f(400+rain_x, rain_start_y)
    glVertex2f(400+rain_x+displacement, rain_end_y)

    glVertex2f(500+rain_x, rain_start_y)
    glVertex2f(500+rain_x+displacement, rain_end_y)

    glVertex2f(600+rain_x, rain_start_y)
    glVertex2f(600+rain_x+displacement, rain_end_y)

    glVertex2f(700+rain_x, rain_start_y)
    glVertex2f(700+rain_x+displacement, rain_end_y)

    glVertex2f(800+rain_x, rain_start_y)
    glVertex2f(800+rain_x+displacement, rain_end_y)

    glEnd()

    # Disable line stippling
    glDisable(GL_LINE_STIPPLE)

    glFlush()

def drawHome():
    glClearColor(currentMode_bg[0], currentMode_bg[1], currentMode_bg[2], 0)

    glLineWidth(5)
    glBegin(GL_LINES)

    glColor3f(currentMode_fg[0], currentMode_fg[1], currentMode_fg[2])

    glVertex2f(-202,-150)
    glVertex2f(202,-150)

    glVertex2f(-200,-150)
    glVertex2f(-200,50)

    glVertex2f(200,-150)
    glVertex2f(200,50)

    glVertex2f(-230,50)
    glVertex2f(230,50)

    glVertex2f(-230,50)
    glVertex2f(0,150)

    glVertex2f(230,50)
    glVertex2f(0,150)

    glVertex2f(-50,-150)
    glVertex2f(-50,0)

    glVertex2f(50,-150)
    glVertex2f(50,0)

    glVertex2f(-52,0)
    glVertex2f(52,0)

    glVertex2f(-170,0)
    glVertex2f(-170,-50)

    glVertex2f(-130,0)
    glVertex2f(-130,-50)

    glVertex2f(-172,-50)
    glVertex2f(-128,-50)

    glVertex2f(-172,0)
    glVertex2f(-128,0)

    glVertex2f(130,0)
    glVertex2f(130,-50)

    glVertex2f(170,0)
    glVertex2f(170,-50)

    glVertex2f(128,0)
    glVertex2f(172,0)
    
    glVertex2f(128,-50)
    glVertex2f(172,-50)

    glEnd()

    glPointSize(8)
    glBegin(GL_POINTS)
    
    glVertex2f(35, -75)

    glEnd()

def display():
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
    drawHome()
    drawRain()

    glutSwapBuffers()

def init():
    #//clear the screen
    glClearColor(currentMode_bg[0], currentMode_bg[1], currentMode_bg[2], 0)
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
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"Assignment problem 1")
init()

glutDisplayFunc(display)
glutIdleFunc(animate)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()