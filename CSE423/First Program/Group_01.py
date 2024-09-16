from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import time

WINDOW_WIDTH  = 1400
WINDOW_HEIGHT = 800

class AABB:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
    
    def collides_with(self, other):
        return (self.x < other.x + other.w and # x_min_1 < x_max_2
                self.x + self.w > other.x  and # x_max_1 > m_min_2
                self.y < other.y + other.h and # y_min_1 < y_max_2
                self.y + self.h > other.y)     # y_max_1 > y_min_2

class Helicopter(AABB):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.critical_point = AABB(self.x+(self.w//2)-2, self.y, 4, 4)
        self.engaged = False
    
    def move_left(self):
        if self.x > 30:
            self.x -= 20
            self.critical_point.x -= 20
        elif self.x > 10:
            self.x -= 10
            self.critical_point.x -= 10
            
    def move_right(self):
        if self.y >= 400:
            if self.x+self.w < WINDOW_WIDTH-30:
                self.x += 20
                self.critical_point.x += 20
            elif self.x+self.w < WINDOW_WIDTH-10:
                self.x += 10
                self.critical_point.x += 10
        else:
            if self.x+self.w < 170:
                self.x += 20
                self.critical_point.x += 20
            elif self.x+self.w < 190:
                self.x += 10
                self.critical_point.x += 10
    
    def move_up(self):
        if self.y+self.h < WINDOW_HEIGHT-30:
            self.y += 20
            self.critical_point.y += 20
    
    def move_down(self):
        if self.x+self.w >= 200:
            if self.y > 430:
                self.y -= 20
                self.critical_point.y -= 20
            elif self.y > 410:
                self.y -= 10
                self.critical_point.y -= 10
        else:
            if self.engaged:
                if self.y > safe_height+30:
                    self.y -= 20
                    self.critical_point.y -= 20
                elif self.y > safe_height+10:
                    self.y -= 10
                    self.critical_point.y -= 10
            else:
                if self.y > safe_height-10 and self.y > 20:
                    self.y -= 20
                    self.critical_point.y -= 20
        

class Building(AABB):
    def __init__(self, x, y, w, h, fire):
        super().__init__(x, y, w, h)
        self.fire = fire


# Global variables
helicopter = Helicopter(WINDOW_WIDTH//2-25, WINDOW_HEIGHT-150, 50, 120)

engaged_tank = None
safe_height = 0
water_tanks = []
for i in range(2):
    line_of_tanks = []
    for j in range(3):
        line_of_tanks.append(AABB(0+(j*50), safe_height, 50, 50))
    water_tanks.append(line_of_tanks)
    safe_height += 50

buildings = []
building_fire_status = [random.randint(0,1) for i in range(4)]
building_fire_status.append(1)
for i in range(5):
    buildings.append(Building(300+(i*200), 0, 190, 300, building_fire_status[i]))
alloted_time = 8 * sum(building_fire_status)


# -----------  MIDPOINT LINE ALGORITHM START  -----------
def draw_line_points(x, y, zone):
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
    draw_line_points(x, y, zone)
    while x < x2:
        if d < 0:
            d = d + dE
            x = x + 1
        else:
            d = d + dNE
            x = x + 1
            y = y + 1
        draw_line_points(x, y, zone)
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
# -----------  MIDPOINT LINE ALGORITHM END  -----------


# ------------ Midpoint circle drawing algorithm start ------------
def draw_circle_points(x, y, a, b):
    glVertex2f(x+a, y+b)
    glVertex2f(y+a, x+b)
    glVertex2f(-y+a, x+b)
    glVertex2f(-x+a, y+b)
    glVertex2f(-x+a, -y+b)
    glVertex2f(-y+a, -x+b)
    glVertex2f(y+a, -x+b)
    glVertex2f(x+a, -y+b)

def drawCircle(a, b, r):
    d = (-r * 4) + 5
    x = r
    y = 0
    draw_circle_points(x, y, a, b)
    while x > y:
        if d < 0:
            d += 8 * y + 12  # dN
            y += 1
        else:
            d += - 8 * x + 8 * y + 20  # dNW
            x -= 1
            y += 1
        draw_circle_points(x, y, a, b)
# ------------ Midpoint circle drawing algorithm end ------------


def draw_helicopter():
    glColor3f(0, 1, 0)  # green
    glPointSize(3)
    glBegin(GL_POINTS)
    
    drawCircle(helicopter.x+(helicopter.w//2), helicopter.y+helicopter.h-(helicopter.w//2), helicopter.w//2)
    drawline(helicopter.x+(helicopter.w//2), helicopter.y+helicopter.h-helicopter.w, helicopter.x+(helicopter.w//2), helicopter.y)

    glEnd()

def draw_building(building):
    if building.fire:
        glColor3f(1, 0, 0)
    else:
        glColor3f(1, 1, 1)

    glPointSize(3)
    glBegin(GL_POINTS)
    
    drawline(building.x, building.y, building.x, building.y+building.h)
    drawline(building.x+building.w, building.y, building.x+building.w, building.y+building.h)
    drawline(building.x, building.y+building.h, building.x+building.w, building.y+building.h)

    glEnd()

def draw_water_tank(tank):
    glColor3f(0, 0, 1)  # blue
    glPointSize(3)
    glBegin(GL_POINTS)
    
    drawline(tank.x, tank.y, tank.x+tank.w, tank.y)
    drawline(tank.x, tank.y, tank.x, tank.y+tank.h)
    drawline(tank.x+tank.w, tank.y, tank.x+tank.w, tank.y+tank.h)
    drawline(tank.x, tank.y+tank.h, tank.x+tank.w, tank.y+tank.h)

    glEnd()


def initialize():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def check_collision(obj_a, obj_b):
    if obj_a.collides_with(obj_b):
        return True
    else:
        return False

def show_screen():
    global engaged_tank, safe_height
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # uncomment the following lines to see safety lines
    # glColor3f(1, 1, 1)
    # glPointSize(1)
    # glBegin(GL_POINTS)
    # drawline(0, WINDOW_HEIGHT-30, WINDOW_WIDTH, WINDOW_HEIGHT-30)
    # drawline(200, 0, 200, 400)
    # drawline(200, 400, WINDOW_WIDTH, 400)
    # glEnd()

    # draw stuffs here
    draw_helicopter()
    for b in buildings:
        draw_building(b)

    for i in range(len(water_tanks)):
        for j in range(len(water_tanks[i])):
            if water_tanks[i][j] is not None:
                draw_water_tank(water_tanks[i][j])
    
    # to draw the engaged tank
    if engaged_tank:
        draw_water_tank(engaged_tank)

    # do not forget to call glutSwapBuffers() at the end of the function
    glutSwapBuffers()

def keyboard_special_keys(key, _, __):
    
    if key == GLUT_KEY_LEFT:
        helicopter.move_left()
    elif key == GLUT_KEY_RIGHT:
        helicopter.move_right()
    elif key == GLUT_KEY_UP:
        helicopter.move_up()
    elif key == GLUT_KEY_DOWN:
        helicopter.move_down()

    glutPostRedisplay()

def mouse_click(button, state, x, y):
    
    mx, my = x, WINDOW_HEIGHT - y

    # do your click detection here using button, state, mx, my
    if button==GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if engaged_tank and mx >= engaged_tank.x and mx <= engaged_tank.x+engaged_tank.w and my >= engaged_tank.y and my <= engaged_tank.y+engaged_tank.h:
            print("Tank released")
            helicopter.engaged = False

    glutPostRedisplay()

def animation():
    global engaged_tank, safe_height

    if sum(building_fire_status) == 0:
        print("You won!")
        glutLeaveMainLoop()
    
    count = 0
    for i in range(len(water_tanks)):
        for j in range(len(water_tanks[i])):
            if water_tanks[i][j] is not None:
                count += 1
    if count == 0 and not engaged_tank:
        print("No tank left!")
        glutLeaveMainLoop()

    if time.process_time() - start_time > alloted_time:
        print("Time's over!")
        glutLeaveMainLoop()
    
    for i in range(len(water_tanks)):
        for j in range(len(water_tanks[i])):
            if water_tanks[i][j] is not None:
                if not helicopter.engaged and check_collision(helicopter.critical_point, water_tanks[i][j]):
                    print("New tank picked up")
                    engaged_tank = water_tanks[i][j]
                    water_tanks[i][j] = None
                    helicopter.engaged = True
                    
                    flag = True            
                    for k in range(len(water_tanks[i])):
                        if water_tanks[i][k] is not None:
                            flag = False
                            break
                    if flag:
                        safe_height -= 50

    if engaged_tank and helicopter.engaged:
        engaged_tank.x = helicopter.x
        engaged_tank.y = helicopter.y-engaged_tank.h
    elif engaged_tank and not helicopter.engaged:
        for i in range(len(buildings)):
            if check_collision(engaged_tank, buildings[i]) and building_fire_status[i] == 1:
                buildings[i].fire = False
                engaged_tank = None
                building_fire_status[i] = 0
                print("Fire extinguished")
                break
        
        if engaged_tank:
            if engaged_tank.y > 0:
                engaged_tank.y -= 15
            else:
                engaged_tank = None
                print("Tank wasted")

    glutPostRedisplay()


start_time = time.process_time()
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Fire Extinguisher Game")

glutDisplayFunc(show_screen)
glutIdleFunc(animation)

glutSpecialFunc(keyboard_special_keys)
glutMouseFunc(mouse_click)

glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()