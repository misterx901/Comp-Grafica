from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


n1, n2, r , M, N = 50, 50, 2, 100, 100

def f(x,y):
    return x**2-y**2

x0, y0, xf, yf = -2, -2, 2, 2

dx, dy = (xf - x0)/M, (yf - y0)/N
cont=0


#FUNCAO F1

def f1(i,j):
    theta = (math.pi*i/(n1-1))-(math.pi/2)
    phi = 2*math.pi*j/(n2-1)
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x,y**2,z


#LOOP

def mesh():
    global cont
    cont+=1
    glPushMatrix()
    glRotatef(cont,1.0,0.0,0.0)
    glBegin(GL_QUAD_STRIP)
    
    for i in range(0,n1//2): 
        for j in range(0,n2): 
            glColor3f(-2.0-(i/n1), i/n1, 255)
            x,y,z = f1(i,j)
            glVertex3f(x,y,z)
            x,y,z = f1(i+1,j)
            glVertex3f(x,y,z)
    glEnd()
    glPopMatrix()

def desenhaParaboloide():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(600,600)
glutCreateWindow("Paraboloide")
glutDisplayFunc(desenhaParaboloide)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.2,0,0.2,0)
gluPerspective(50,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()