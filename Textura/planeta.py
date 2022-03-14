from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png
import math
import numpy


ESCAPE = '\033'

xRotate = 0.0
yRotate = 0.0
zRotate = 0.0
dimX = 0.1
dimY = 0
dimZ = 0
n1 = 50
n2 = 50
dist = 0.5

a = 0




# texture = []
def f1(i,j,theta,phi):
    
    x = dist*math.cos(theta)*math.cos(phi)
    y = dist*math.sin(theta)
    z = dist*math.cos(theta)*math.sin(phi)
    return x,y,z

def s(theta):
    return theta/(2*math.pi)
def t(phi):
    return ((phi/math.pi)+(1/2))

def LoadTextures():
    global texture
    texture = glGenTextures(2) # Gera 2 IDs para as texturas

    reader = png.Reader(filename='mapa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


stars = []
total_stars = 1000
starts_range = 100

def draw_stars():
    
    glPushMatrix()

    glTranslatef(0,0,-30)

    glBegin(GL_POINTS)
    for i in range(total_stars):
        eixoX = stars[0][i]*starts_range
        eixoY = stars[1][i]*starts_range
        glVertex3fv((eixoX, eixoY, 0))
        glVertex3fv((-eixoY, -eixoX, 0))
        glVertex3fv((-eixoX, eixoY, 0))
        glVertex3fv((eixoY, -eixoX, 0))
    glEnd()
    
    glPopMatrix()

def loadRandomStars():

    x  = list(numpy.random.rand(1, total_stars)[0])
    y  = list(numpy.random.rand(1, total_stars)[0])
    stars.append(x)
    stars.append(y)

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1
    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xRotate, yRotate, zRotate, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                              
    glTranslatef(0.0,0.0,-3.0)
    glRotatef(xRotate,1.0,0.0,0.0)          
    glRotatef(yRotate,0.0,1.0,0.0)           
    glRotatef(zRotate,0.0,0.0,1.0) 
    draw_stars()
    glBindTexture(GL_TEXTURE_2D, texture[0])              
    for i in range(0,n1): 
        glBegin(GL_QUAD_STRIP)

        for j in range(0,n2): 
            theta = (math.pi*i/(n1-1))-(math.pi/2)
            phi = 2*math.pi*j/(n2-1)
            x,y,z = f1(i,j,theta,phi)
            glTexCoord2f(s(phi), t(theta)); glVertex3f(x,y,z)
            theta = (math.pi*(i+1)/(n1-1))-(math.pi/2)
            x,y,z = f1(i+1,j,theta,phi)
            glTexCoord2f(s(phi), t(theta)); glVertex3f(x,y,z)
        glEnd()
    
    xRotate = xRotate + 0.1                
    yRotate = yRotate + 0.1                 
    zRotate = zRotate + 0.1                 

    glutSwapBuffers()

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Textura")
    loadRandomStars()
    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    
    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print("Hit ESC key to quit.")
    main()