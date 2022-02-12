from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cont = 0
N = 5    
H = 7
r = 4
  

cores = ((-1,1,-1),
         (1,0,1),
         (1,0,-1),
         (1,0,1),
         (1,0,0),
         (0,-1,1),
         (1,0,1),
         (1,-1,1))

def piramide():
    global cont
    cont+=1
    pontosBase = []
    angulo = (2*math.pi)/N

    glPushMatrix()
    glTranslatef(0,-3,0)
    glRotatef(cont,0.0,1.0,0.0)
    glRotatef(-90,1.0,0.0,0.0)
    glColor3fv(cores[0])

  
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = r * math.cos(i*angulo)
        y = r * math.sin(i*angulo)
        pontosBase += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

   
    glBegin(GL_TRIANGLES)
    for i in range(0,N):
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(0.0,0.0,H)
        glVertex3f(pontosBase[i][0],pontosBase[i][1],0.0)
        glVertex3f(pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
    glEnd()

    glPopMatrix()


def desenhaPiramide():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    piramide()
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide")
glutDisplayFunc(desenhaPiramide)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()