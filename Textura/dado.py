import sys
sys.path.append('../')
from texture import Texture
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


textures_files = {
    'dice': 'dado.png',
}

tx = Texture(textures_files, 'Dado', 1000, 800)

ESCAPE = b'\033'

xRotate = yRotate = zRotate = 0.0
direction = (0.1, 0, 0)

def DrawGLScene():
    global xRotate, yRotate, zRotate, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   
    glClearColor(0.5,0.5,0.5,1.0)            
    glTranslatef(0.0,0.0,-5.0)
    glRotatef(xRotate,1.0,0.0,0.0)          
    glRotatef(yRotate,0.0,1.0,0.0)           
    glRotatef(zRotate,0.0,0.0,1.0) 
    
    glBindTexture(GL_TEXTURE_2D, tx.textures['dice'])
    glBegin(GL_QUADS)              
    
    # Front Face 1
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(0.0, 1/2); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(1/3, 1/2); glVertex3f( 1.0,  1.0,  1.0)   
    glTexCoord2f(1/3, 0.0); glVertex3f(-1.0,  1.0,  1.0)  

    # Back Face 6
    glTexCoord2f(2/3, 1/2); glVertex3f(-1.0, -1.0, -1.0)    
    glTexCoord2f(2/3, 1.0); glVertex3f(-1.0,  1.0, -1.0)    
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    
    glTexCoord2f(1.0, 1/2); glVertex3f( 1.0, -1.0, -1.0)   
    
    # Top Face 2
    glTexCoord2f(1/3, 0); glVertex3f(-1.0,  1.0, -1.0)   
    glTexCoord2f(1/3, 1/2); glVertex3f(-1.0,  1.0,  1.0)    
    glTexCoord2f(2/3, 1/2); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(2/3, 0); glVertex3f( 1.0,  1.0, -1.0)   

    # Bottom Face 5      
    glTexCoord2f(1/3, 1/2); glVertex3f(-1.0, -1.0, -1.0)   
    glTexCoord2f(1/3, 1); glVertex3f( 1.0, -1.0, -1.0)   
    glTexCoord2f(2/3, 1); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(2/3, 1/2); glVertex3f(-1.0, -1.0,  1.0)    
    
    # Right face 3
    glTexCoord2f(2/3, 0.0); glVertex3f( 1.0, -1.0, -1.0)    
    glTexCoord2f(2/3, 1/2); glVertex3f( 1.0,  1.0, -1.0)   
    glTexCoord2f(1, 1/2); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(1, 0.0); glVertex3f( 1.0, -1.0,  1.0)  
    
    # Left Face 4
    glTexCoord2f(0, 1/2); glVertex3f(-1.0, -1.0, -1.0)  
    glTexCoord2f(0, 1); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(1/3, 1); glVertex3f(-1.0,  1.0,  1.0)   
    glTexCoord2f(1/3, 1/2); glVertex3f(-1.0,  1.0, -1.0)   
    
    glEnd()                # Done Drawing The Cube
    
    xRotate = xRotate + 0.01                 # X rotation
    yRotate = yRotate + 0.01                 # Y rotation
    zRotate = zRotate + 0.01                 # Z rotation

    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dimX, dimY, dimZ
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == b'x' or tecla == b'X':
        dimX=1
        dimY=0
        dimZ=0
    elif tecla == b'y' or tecla == b'Y':   
        dimX=0
        dimY=1
        dimZ=0
    elif tecla == b'z' or tecla == b'Z':
        dimX=0
        dimY=0
        dimZ=1


def specialKeyPressed(tecla, x, y):
    global xRotate, yRotate, zRotate, dimX, dimY, dimZ
    if tecla == GLUT_KEY_LEFT:
        print ("ESQUERDA")

        yRotate -= dimY

    elif tecla == GLUT_KEY_RIGHT:
        print ("DIREITA")
        yRotate += dimY

    elif tecla == GLUT_KEY_UP:
        print ("CIMA")
    elif tecla == GLUT_KEY_DOWN:
        print ("BAIXO")



tx.main(DrawGLScene, keyPressed, specialKeyPressed)