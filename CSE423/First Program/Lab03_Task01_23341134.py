from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# ------------ Midpoint circle drawing algorithm start ------------
def draw_points(x, y, a, b):
    glVertex2f(x+a, y+b)
    glVertex2f(y+a, x+b)
    glVertex2f(-y+a, x+b)
    glVertex2f(-x+a, y+b)
    glVertex2f(-x+a, -y+b)
    glVertex2f(-y+a, -x+b)
    glVertex2f(y+a, -x+b)
    glVertex2f(x+a, -y+b)

def drawCircle(crcl):
    d = (-crcl.r * 4) + 5
    x = crcl.r
    y = 0
    draw_points(x, y, crcl.x, crcl.y)
    while x > y:
        if d < 0:
            d += 8 * y + 12  # dN
            y += 1
        else:
            d += - 8 * x + 8 * y + 20  # dNW
            x -= 1
            y += 1
        draw_points(x, y, crcl.x, crcl.y)
# ------------ Midpoint circle drawing algorithm end ------------

W_Width, W_Height = 500,500
growth_speed = 0.5
circles = []
paused = False


def distance(a, b, x, y):
    return (((x-a)**2)+((y-b)**2))**0.5

class Circle:
    def __init__(self, x, y):
        self.r=0
        self.x=x
        self.y=y
        self.max_r = max([distance(x,y,-W_Width/2,-W_Height/2), distance(x,y,W_Width/2,-W_Height/2), distance(x,y,-W_Width/2,W_Height/2), distance(x,y,W_Width/2,W_Height/2)])
        print(x, y)
    
    def increase_radius(self):
        self.r += growth_speed
    
    def __del__(self):
        del self.r
        del self.x
        del self.y
        del self.max_r
        del self


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
            print("Resumed")
        else:
            paused = True
            print("Paused")

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global growth_speed

    if not paused:
        if key==GLUT_KEY_LEFT:
            growth_speed += 1
            print("Increasing speed")
        elif key== GLUT_KEY_RIGHT:
            if growth_speed > 1:
                growth_speed -= 1
                print("Decreasing speed")
    
    glutPostRedisplay()


def mouseListener(button, state, x, y):
    if not paused:        
        if button==GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            a, b = convert_coordinate(x,y)
            circles.append(Circle(a, b))
            print("New circle added\nNumber of circles present :", len(circles))

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
    glPointSize(5)
    glColor3f(0.67, 0.84, 0.9)
    glBegin(GL_POINTS)
    for c in circles:
        if c.r > c.max_r:
            circles.remove(c)
            del c
            print("Circle removed\nNumber of circles present :", len(circles))
        else:
            drawCircle(c)
    glEnd()
    
    glutSwapBuffers()


def animate():
    if not paused:
        for c in circles:
            c.increase_radius()
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
