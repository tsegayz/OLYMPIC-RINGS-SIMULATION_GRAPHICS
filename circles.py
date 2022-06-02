from turtle import color
import pyglet
import math
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 

window = pyglet.window.Window(800,600,"Olyompic Rings Simulation")

def draw_circle(max, xorig, yorig, rad):
    
    global verts
    verts = []
    angle = 360 / max
    

    for i in range(max):
        angle_rad = ( angle * i) * (math.pi/180)
        cosine = math.cos(angle_rad) 
        sine = math.sin(angle_rad)
        
        x = cosine *rad - sine*rad + xorig
        y = sine *rad + cosine*rad + yorig
        glPointSize(2)
        verts.append(int(x))
        verts.append(int(y))

draw_circle(500, 220, 350, 50)


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

            z+=2

pyglet.clock.schedule_interval(update, 1/120)


pyglet.app.run()