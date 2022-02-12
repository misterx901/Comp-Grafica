from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

r = 3
r2 = 3
N = 5
H = 6
cont=0

cores = ((-1,1,-1),
         (1,0,1),
         (1,0,-1),
         (1,0,1),
         (1,0,0),
         (0,-1,1),
         (1,0,1),
         (1,-1,1))

def prisma():
    global cont
    pontosBase = []
    pontosBase2 = []
    angulo = (2*math.pi)/N
    cont+=1
    
    glPushMatrix()
    glTranslatef(0,-3,0)
    glRotatef(cont,0.0,1.0,0.0)
    glRotatef(-40,1.0,0.0,0.0)
    glColor3fv(cores[0])

    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = r * math.cos(i*angulo)
        y = r * math.sin(i*angulo)
        pontosBase += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for j in range(0,N):
        x2 = r2 * math.cos(j*angulo)
        y2 = r2 * math.sin(j*angulo)
        pontosBase2 += [(x2,y2)]
        glVertex3f(x2,y2,H)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(0,N):
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(pontosBase[i][0],pontosBase[i][1],0.0)
        glVertex3f(pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
        glVertex3f(pontosBase2[i][0],pontosBase2[i][1],H)
        glVertex3f(pontosBase2[(i+1)%N][0],pontosBase2[(i+1)%N][1],H)
    glEnd()

    glPopMatrix()

def desenhaPrisma():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    prisma()
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Prisma")
glutDisplayFunc(desenhaPrisma)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(70,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()