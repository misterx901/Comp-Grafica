from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys
import math

def calculaFace(v0, v1, v2):
    x = 0
    y = 1
    z = 2

    U = (v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = (v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ((U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return (N[x]/NLength, N[y]/NLength, N[z]/NLength)

def Prisma():
    r = 2
    pontosBase = []
    angulo = (2*math.pi)/5

    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(-110,1.0,0.0,0.0)

    # BASE
    glBegin(GL_POLYGON)

    for i in range(0,5):
        x = r * math.cos(i*angulo)
        y = r * math.sin(i*angulo)
        pontosBase += [ (x,y) ]
        glVertex3f(x,y,0.0)

    h = (pontosBase[0][0], pontosBase[0][1], 0)
    j = (pontosBase[1][0], pontosBase[1][1], 0)
    k = (pontosBase[2][0], pontosBase[2][1], 0)

    glNormal3fv(calculaFace(h,j,k))

    glEnd()

    # TOPO
    glBegin(GL_POLYGON)
    for x,y in pontosBase:
        glVertex3f(1*x,1*y, 4)
    
    h = (pontosBase[0][0], pontosBase[0][1], 4)
    j = (pontosBase[1][0], pontosBase[1][1], 4)
    k = (pontosBase[2][0], pontosBase[2][1], 4)

    glNormal3fv(calculaFace(h,j,k))
    glEnd()

    # LATERAL
    glBegin(GL_QUADS)
    for i in range(0,5):
        h = (pontosBase[i][0], pontosBase[i][1],0.0)
        j = (1*pontosBase[i][0],1*pontosBase[i][1],4)
        k = (1*pontosBase[(i+1)%5][0],1*pontosBase[(i+1)%5][1],4)
        l = (pontosBase[(i+1)%5][0],pontosBase[(i+1)%5][1],0.0)

        glNormal3fv(calculaFace(h,j,k))

        glVertex3fv(h)
        glVertex3fv(j)
        glVertex3fv(k)
        glVertex3fv(l)
    glEnd()

    glPopMatrix()

    
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,3,1,0)
    Prisma()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt( 10,0,0, 0,0,0,     0,1,0 )

def init():
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (50,)
    light_position = (10, 0, 0)
    glClearColor(0.7,0.7,0.7,0.0)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Prisma")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()
