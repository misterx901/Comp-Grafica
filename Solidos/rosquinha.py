from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

angle = 0
density = 50
rotation_speed = 2
global_radius = 2
hole_radius = 1
color = 255


def rosquinha(u, v):
    theta = ( u * 2 * pi) / (density - 1)
    phi = (v * 2 * pi) / (density - 1)
    x = (global_radius + hole_radius * cos(theta)) * cos(phi)
    y = (global_radius + hole_radius * cos(theta)) * sin(phi)
    z = (hole_radius * sin(theta))

    return x, y, z


def desenharRosquinha():
    global angle
    angle += rotation_speed
    glTranslatef(1,0,0)
    glRotatef(angle,0,1,0)

    for i in range(density):    
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(density):
            glColor3f(1, 1, 1)
            glVertex3fv(rosquinha(i,j))
            glVertex3fv(rosquinha(i - 1,j))
        glEnd()


def draw():    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()    
    desenharRosquinha()    
    glPopMatrix()
    
    glutSwapBuffers()

 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Rosquinha")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(48,800.0/400.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()
