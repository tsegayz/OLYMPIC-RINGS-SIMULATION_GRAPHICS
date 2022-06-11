import pyglet
import math
from OpenGL.GL import *
from OpenGL.GLU import *


window = pyglet.window.Window(800, 600, "Olyompic Rings Simulation")


def draw_circle(max, xorig, yorig, rad):

    global verts
    verts = []
    angle = 360 / max

    for i in range(max):
        angle_rad = (angle * i) * (math.pi/180)
        cosine = math.cos(angle_rad)
        sine = math.sin(angle_rad)

        x = cosine * rad - sine*rad + xorig
        y = sine * rad + cosine*rad + yorig

        verts.append(int(x))
        verts.append(int(y))


def draw_circle1(max, xorig, yorig, rad):

    global verts1
    verts1 = []
    angle = 360 / max

    for i in range(max):
        angle_rad = (angle * i) * (math.pi/180)
        cosine = math.cos(angle_rad)
        sine = math.sin(angle_rad)

        x = cosine * rad - sine*rad + xorig
        y = sine * rad + cosine*rad + yorig
        glPointSize(2)
        verts1.append(int(x))
        verts1.append(int(y))


def draw_circle2(max, xorig, yorig, rad):

    global verts2
    verts2 = []
    angle = 360 / max

    for i in range(max):
        angle_rad = (angle * i) * (math.pi/180)
        cosine = math.cos(angle_rad)
        sine = math.sin(angle_rad)

        x = cosine * rad - sine*rad + xorig
        y = sine * rad + cosine*rad + yorig
        glPointSize(2)
        verts2.append(int(x))
        verts2.append(int(y))


def draw_circle3(max, xorig, yorig, rad):

    global verts3
    verts3 = []
    angle = 360 / max

    for i in range(max):
        angle_rad = (angle * i) * (math.pi/180)
        cosine = math.cos(angle_rad)
        sine = math.sin(angle_rad)

        x = cosine * rad - sine*rad + xorig
        y = sine * rad + cosine*rad + yorig
        glPointSize(2)
        verts3.append(int(x))
        verts3.append(int(y))

def draw_circle4(max, xorig, yorig, rad):
    
    global verts4
    verts4 = []
    angle = 360 / max
    
    for i in range(max):
        angle_rad = ( angle * i) * (math.pi/180)
        cosine = math.cos(angle_rad) 
        sine = math.sin(angle_rad)
        
        x = cosine *rad - sine*rad + xorig
        y = sine *rad + cosine*rad + yorig
        
        verts4.append(int(x))
        verts4.append(int(y))


draw_circle(500, 220, 350, 50)
draw_circle1(500, 390, 350, 50)
draw_circle2(500, 300, 270, 50)
draw_circle3(500, 480, 270, 50)
draw_circle4(500, 565, 350, 50)


z = 0


def update(t):

    glPointSize(10)
    global z
    # verts = np.multiply(verts, v)
    if(z < len(verts) - 1):

        glColor(0.0, 0.0, 1.0)
        glBegin(GL_POINTS)
        glVertex2f(verts[z], verts[z+1])
        glEnd()

        z += 2
    if(z < len(verts1) - 1):
        glColor(1.0, 1.0, 1.0)
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                             ('v2i', (verts1[z], verts1[z+1])))
        z += 2
    if(z < len(verts2) - 1):
        glColor(1.0, 1.0, 0.0)
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                             ('v2i', (verts2[z], verts2[z+1])))
        z += 2
    if(z < len(verts3) - 1):
        glColor(0.0, 1.0, 0.0)
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                             ('v2i', (verts3[z], verts3[z+1])))
        z += 2
        if(z < len(verts4) - 1):
            glColor(1.0, 0.0, 0.0)
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (verts4[z], verts4[z+1])))
            z+=2




pyglet.clock.schedule_interval(update, 1/120)

pyglet.app.run()
