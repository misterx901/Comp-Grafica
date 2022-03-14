from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import math 
import sys
import random

lado = random.randrange(3, 8)

def piramide():
	height = 4

	ladoTamanho = (2*math.pi)/lado
	vertices = []

	glPushMatrix()
	glTranslatef(0,-2,0)
	glRotatef(-110,1.0,0.0,0.0)
	# Creating and drawing down vertices
	glBegin(GL_POLYGON)
	for i in range(0,lado):
		x = 3 * math.cos(i*ladoTamanho) - 2
		y = 3 * math.sin(i*ladoTamanho) - 2
		vertices += [ (x,y) ]

		glVertex3f(x,y,0.0)
	glEnd()

	#Drawing side faces
	glBegin(GL_TRIANGLES)
	for i in range(0,lado):
		glNormal3fv(calculaNormalFace( (vertices[i][0],vertices[i][1],0.0), (-2,-2,height), (vertices[(i+1)%lado][0],vertices[(i+1)%lado][1],0.0)))
		glVertex3f(vertices[i][0],vertices[i][1],0.0)
		glVertex3f(-2,-2,height)
		glVertex3f(vertices[(i+1)%lado][0],vertices[(i+1)%lado][1],0.0)
	glEnd()

	glPopMatrix()

def calculaNormalFace(a, b, c):
    U = ( c[0]-a[0], c[1]-a[1], c[2]-a[2] )
    V = ( b[0]-a[0], b[1]-a[1], b[2]-a[2] )
    N = ( (U[1]*V[2]-U[2]*V[1]),(U[2]*V[0]-U[0]*V[2]),(U[0]*V[1]-U[1]*V[0]))
    NLength = sqrt(N[0]*N[0]+N[1]*N[1]+N[2]*N[2])
    return ( N[0]/NLength, N[1]/NLength, N[2]/NLength)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    piramide()
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

    gluLookAt(10,0,0,0,0,0,0,1,0)

def init():
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (50,)
    light_position = (5.0, 5.0, 5.0, 0.0)
    glClearColor(0.7,0.7,0.7,0.0)
    glShadeModel(GL_FLAT)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide")
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutTimerFunc(50,timer,1)
init()
glutMainLoop()

