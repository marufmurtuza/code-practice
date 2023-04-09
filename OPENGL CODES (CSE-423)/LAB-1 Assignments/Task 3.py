# Task 3
# Maruf Bin Murtuza
# 23141042
# Sec-03

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def drawID():
    glLineWidth(5) 
    glBegin(GL_LINES)

    # 2
    glColor3f(1.0, 0.0, 0.0)

    glVertex2f(30,450)
    glVertex2f(60,450)

    glVertex2f(60,450)
    glVertex2f(60,420)

    glVertex2f(30,420)
    glVertex2f(60,420)

    glVertex2f(30,420)
    glVertex2f(30,390)

    glVertex2f(30,390)
    glVertex2f(60,390)

    # 3
    glColor3f(0.0, 0.0, 1.0)

    glVertex2f(80,450)
    glVertex2f(110,450)

    glVertex2f(110,450)
    glVertex2f(110,420)

    glVertex2f(80,420)
    glVertex2f(110,420)

    glVertex2f(110,420)
    glVertex2f(110,390)

    glVertex2f(80,390)
    glVertex2f(110,390)

    # 1
    glColor3f(0.0, 1.0, 0.0)

    glVertex2f(150,450)
    glVertex2f(150,390)

    # 4
    glColor3f(1.0, 1.0, 0.0)

    glVertex2f(170,450)
    glVertex2f(170,420)

    glVertex2f(170,420)
    glVertex2f(200,420)

    glVertex2f(200,450)
    glVertex2f(200,390)

    # 1
    glColor3f(1.0, 0.0, 1.0)

    glVertex2f(240,450)
    glVertex2f(240,390)

    # 0
    glColor3f(0.5, 0.5, 0.5)

    glVertex2f(260,450)
    glVertex2f(260,390)

    glVertex2f(260,450)
    glVertex2f(290,450)

    glVertex2f(290,450)
    glVertex2f(290,390)

    glVertex2f(260,390)
    glVertex2f(290,390)

    # 4
    glColor3f(1.0, 1.0, 1.0)

    glVertex2f(330,450)
    glVertex2f(330,420)

    glVertex2f(330,420)
    glVertex2f(360,420)

    glVertex2f(360,450)
    glVertex2f(360,390)

    # 2
    glColor3f(0.2, 1.0, 1.0)

    glVertex2f(380,450)
    glVertex2f(410,450)

    glVertex2f(410,450)
    glVertex2f(410,420)

    glVertex2f(380,420)
    glVertex2f(410,420)

    glVertex2f(380,420)
    glVertex2f(380,390)

    glVertex2f(380,390)
    glVertex2f(410,390)

    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    drawID()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Lab01 - Task03 - Maruf Bin Murutza")
glutDisplayFunc(showScreen)

glutMainLoop()
