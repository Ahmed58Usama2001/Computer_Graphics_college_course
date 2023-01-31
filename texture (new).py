
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import pygame

global texture

def init():
    global texture
    
    glClearColor(0.7, 0.7, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    

    texture = glGenTextures(5)  # Generate 5 textures
    

#######################################################################################################
    # Create MipMapped Texture
    imgload = pygame.image.load("trees.bmp")
    img = pygame.image.tostring(imgload, "RGBA", 1) # 0) # Serializing the image to a string
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) # GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) # GL_CLAMP)
    # gluBuild2DMipmaps( target, internalFormat,  width,  height,  format, type,  raw_image)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)  # try this
    
    
#######################################################################################################
    
    imgload = pygame.image.load("grass.bmp")
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[1])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR) # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA,GL_UNSIGNED_BYTE, img)

    #glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA,GL_UNSIGNED_BYTE, img)
    #glGenerateMipmap(GL_TEXTURE_2D)
    

#######################################################################################################
    
    imgload = pygame.image.load("wood.jpg")
    img = pygame.image.tostring(imgload, "RGBA", 1) # try 0)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[2])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) # GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) # GL_CLAMP)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA,GL_UNSIGNED_BYTE, img)


#######################################################################################################
    
    imgload = pygame.image.load("chess.png")
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[3])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) # GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) # GL_CLAMP)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0 , GL_RGBA,GL_UNSIGNED_BYTE, img)

#################################################################################################################3

    imgload = pygame.image.load("wall.jpg")
    #imgload = pygame.image.load("sky.bmp")
    img = pygame.image.tostring(imgload, "RGBA", 1) 
    width = imgload.get_width()
    height = imgload.get_height()

    # "Bind" the newly created texture : all future texture functions will modify this texture
    glBindTexture(GL_TEXTURE_2D, texture[4])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) # GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) # GL_CLAMP)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA,GL_UNSIGNED_BYTE, img)

    

    
    glEnable(GL_TEXTURE_2D)


    glBindTexture(GL_TEXTURE_2D, texture[0]) # try texture[1] & texture[2] & texture[3] & texture[4]
    

        
def draw():
    global texture
    
    glClear(GL_COLOR_BUFFER_BIT)
    
    glColor(1,1,1)

    # "glDeleteTextures" deletes the first n textures named by the elements of the array "texture". After a texture is deleted, it has no contents.
    #glDeleteTextures(2,texture) # try to uncomment this line (deletes two texture objects starting from the address "texture[0]".)
    #glDeleteTextures(1,texture+2) # try to uncomment this line (delete one texture object starting from the address "texture[2]". )

    
    
    # you can use the whole texture
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-0.75, -0.75, 0)
    
    glTexCoord(1, 0)
    glVertex(0.75, -0.75, 0)
    
    glTexCoord(1, 1)
    glVertex(0.75, 0.75, 0)
    
    glTexCoord(0, 1)
    glVertex(-0.75, 0.75, 0)

    glEnd()
    
    
    '''
    # Part of the texture
    # you can use a part of the texture
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-0.75, -0.75, 0)
    
    glTexCoord(0.5, 0)
    glVertex(0.75, -0.75, 0)
    
    glTexCoord(0.5, 1) #1,1
    glVertex(0.75, 0.75, 0)
    
    glTexCoord(0, 1)
    glVertex(-0.75, 0.75, 0)

    glEnd()
    '''
    
    '''
    # Repeated Texture
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-0.75, -0.75, 0)
    
    glTexCoord(10, 0)
    glVertex(0.75, -0.75, 0)
    
    glTexCoord(10, 10) #1,1
    glVertex(0.75, 0.75, 0)
    
    glTexCoord(0, 10)
    glVertex(-0.75, 0.75, 0)

    glEnd()
    '''

    '''
    glBegin(GL_TRIANGLES)

    glTexCoord(0, 0)
    glVertex(-0.75, -0.75, 0)
    
    glTexCoord(1, 0)
    glVertex(0.75, -0.75, 0)
    
    glTexCoord(1, 1) #1,1
    glVertex(0.75, 0.75, 0)
    
    
    #glVertex(-0.75, 0.75, 0)

    glEnd()
    '''

    '''
    # Smal QUADS for Mipmap
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-0.02, -0.02, 0)
    
    glTexCoord(1, 0)
    glVertex(0.02, -0.02, 0)
    
    glTexCoord(1, 1) #1,1
    glVertex(0.02, 0.02, 0)
    
    glTexCoord(0, 1)
    glVertex(-0.02, 0.02, 0)

    glEnd()
    '''

    glFlush()

    glDeleteTextures(5,texture)


    

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"Texture")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()
    
main()

