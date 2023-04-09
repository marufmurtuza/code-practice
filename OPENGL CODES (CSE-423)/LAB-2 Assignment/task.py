from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def findinitzone(dx, dy):
    if (dx > -1 and dy > -1):
        if (abs(dx) >= abs(dy)):return 0
        else:return 1
    elif (dx < 0 and dy > -1):
        if (abs(dx) < abs(dy)):return 2
        else:return 3
    elif (dx < 0 and dy < 0):
        if (abs(dx) >= abs(dy)):return 4
        else:return 5
    else:
        if abs(dx) < abs(dy):return 6
        else:return 7


def con2z0(x1, y1, x2, y2, zone):
    a = 0
    b = 0
    c = 0
    d = 0

    if zone == 0:
        a = x1
        b = y1
        c = x2
        d = y2

    elif zone == 1:
        a = y1
        b = x1
        c = y2
        d = x2

    elif zone == 2:
        a = y1
        b = -x1
        c = y2
        d = -x2

    elif zone == 3:
        a = -x1
        b = y1
        c = -x2
        d = y2

    elif zone == 4:
        a = -x1
        b = -y1
        c = -x2
        d = -y2

    elif zone == 5:
        a = -y1
        b = -x1
        c = -y2
        d = -x2

    elif zone == 6:
        a = -y1
        b = x1
        c = -y2
        d = x2

    elif zone == 7:
        a = x1
        b = -y1
        c = x2
        d = -y2

    return a, b, c, d


def drawline(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = findinitzone(dx, dy)

    x1, y1, x2, y2 = con2z0(x1, y1, x2, y2, zone)
    X0 = []
    Y0 = []
    d = []

    dx = x2 - x1
    dy = y2 - y1
    D = 2 * dy - dx

    d = d + [D]
    dNE = 2 * (dy - dx)
    dE = 2 * dy

    x = x1
    y = y1
    while x <= x2:
        a = x
        b = y
        X0 += [x]
        Y0 += [y]

        a, b = con2initialzone(a, b, zone)
        draw_points(a, b)
        x = x + 1
        if D > 0:
            y = y + 1
            D = D + dNE
        else:
            D = D + dE
            d += [D]


def con2initialzone(x, y, zone):
    if zone == 0:return x, y
    if zone == 1:return y, x
    if zone == 2:return -y, x
    if zone == 3:return -x, y
    if zone == 4:return -x, -y
    if zone == 5:return -y, -x
    if zone == 6:return y, -x
    if zone == 7:return x, -y


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    
    # 4
    glColor3f(1, 1, 0)
    drawline(100, 250, 100, 370) # Left |
    drawline(100, 250, 220, 250) # Mid -
    drawline(220, 120, 220, 370) # Right | 
    
     
    # 2
    glColor3f(0, 1, 0)
    drawline(270, 370, 370, 370) # Upper -
    drawline(370, 370, 370, 250) # Right |
    drawline(270, 250, 370, 250) # Mid -
    drawline(270, 250, 270, 120) # Left |
    drawline(270, 120, 370, 120) # Lower -


    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"23141042 - LAB - 02")
glutDisplayFunc(showScreen)

glutMainLoop()

