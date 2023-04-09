import math

from OpenGL.GL import *
from OpenGL.GLUT import *


def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-900.0, 900, -900.0, 900, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def DrawPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2d(x, y)
    glEnd()


def DrawCirclepoints(x, y, x_c, y_c):
    glBegin(GL_POINTS)
    x_0, y_0 = y, x
    x_1, y_1 = x, y
    x_2, y_2 = -x, y
    x_3, y_3 = -y, x
    x_4, y_4 = -y, -x
    x_5, y_5 = -x, -y
    x_6, y_6 = x, -y
    x_7, y_7 = y, -x
    glVertex2f(x_0 + x_c, y_0 + y_c)
    glVertex2f(x_1 + x_c, y_1 + y_c)
    glVertex2f(x_2 + x_c, y_2 + y_c)
    glVertex2f(x_3 + x_c, y_3 + y_c)
    glVertex2f(x_4 + x_c, y_4 + y_c)
    glVertex2f(x_5 + x_c, y_5 + y_c)
    glVertex2f(x_6 + x_c, y_6 + y_c)
    glVertex2f(x_7 + x_c, y_7 + y_c)

    glEnd()


def drawCircle(radius, x_c, y_c):
    d = 1 - radius
    x = 0
    y = radius
    DrawCirclepoints(x, y, x_c, y_c)
    while x < y:
        if d <= 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * x - 2 * y + 5
            x += 1
            y -= 1
        DrawCirclepoints(x, y, x_c, y_c)


def showScreen():
    glColor(1,1,0)
    radius = 300
    drawCircle(radius, 0, 0)
    drawCircle(radius // 2, radius // 2, 0)
    drawCircle(radius // 2, ((radius // 2) * math.cos(360 / 9)), ((radius // 2) * math.sin(360 / 9)))
    drawCircle(radius // 2, -radius // 2, 0)
    drawCircle(radius // 2, -((radius // 2) * math.cos(360 / 9)), ((radius // 2) * math.sin(360 / 9)))
    drawCircle(radius // 2, 0, radius // 2)
    drawCircle(radius // 2, ((radius // 2) * math.cos(360 / 9)), -((radius // 2) * math.sin(360 / 9)))
    drawCircle(radius // 2, 0, -radius // 2)
    drawCircle(radius // 2, -((radius // 2) * math.cos(360 / 9)), -((radius // 2) * math.sin(360 / 9)))

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow("23141042")
glutDisplayFunc(showScreen)

init()

glutMainLoop()
