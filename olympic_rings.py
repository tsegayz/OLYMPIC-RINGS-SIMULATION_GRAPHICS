import pyglet
import math
from OpenGL.GL import *
from OpenGL.GLU import *




# creating class Olyompics which creates pyglet window with super attributes 
class Olyompics(pyglet.window.Window):
    def __init__(self,width,height,title,max,radius):
        super().__init__(width,height,title)
        self.width=width
        self.height=height
        self.max=max
        self.radius=radius
        self.angle=360/self.max
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1,1,1,1)

    # creating the text olyompics and animation 
    label = pyglet.text.Label ('Olympics',
                          font_name='Times New Roman',
                          font_size = 50,
                          x = 300, y = 200,
                        ) 
    label.color = (255, 0, 0, 200)   
    animation=pyglet.image.load_animation('image/torch.png')
    animSprite=pyglet.sprite.Sprite(animation)


    def draw_circle(self,xorigin,yorigin):
        self.xorigin=xorigin
        self.yorigin=yorigin
        
        # global verts
        self.verts = []
        # angle = 360 / max

        for i in range(self.max):
            angle_in_rad = (self.angle * i) * (math.pi/180)
            cosine = math.cos(angle_in_rad)
            sine = math.sin(angle_in_rad)

            x = cosine * self.radius - sine*self.radius + xorigin
            y = sine * self.radius + cosine*self.radius + yorigin

            self.verts.append(int(x))
            self.verts.append(int(y))


    def draw_circle1(self,xorigin,yorigin):
        self.xorigin=xorigin
        self.yorigin=yorigin
        # global verts1
        self.verts1 = []
        

        for i in range(self.max):
            angle_in_rad = (self.angle * i) * (math.pi/180)
            cosine = math.cos(angle_in_rad)
            sine = math.sin(angle_in_rad)

            x = cosine * self.radius - sine*self.radius + xorigin
            y = sine * self.radius + cosine*self.radius + yorigin
            self.verts1.append(int(x))
            self.verts1.append(int(y))


    def draw_circle2(self, xorigin, yorigin):
        self.xorigin=xorigin
        self.yorigin=yorigin
        # global verts2
        self.verts2 = []
        # angle = 360 / max

        for i in range(self.max):
            angle_in_rad = (self.angle * i) * (math.pi/180)
            cosine = math.cos(angle_in_rad)
            sine = math.sin(angle_in_rad)

            x = cosine * self.radius - sine*self.radius + xorigin
            y = sine * self.radius + cosine*self.radius + yorigin
            self.verts2.append(int(x))
            self.verts2.append(int(y))


    def draw_circle3(self, xorigin, yorigin):
        self.xorigin=xorigin
        self.yorigin=yorigin
        # global verts3
        self.verts3 = []
        # angle = 360 / max

        for i in range(self.max):
            angle_in_rad = (self.angle * i) * (math.pi/180)
            cosine = math.cos(angle_in_rad)
            sine = math.sin(angle_in_rad)

            x = cosine * self.radius - sine*self.radius + xorigin
            y = sine * self.radius + cosine*self.radius + yorigin
        
            self.verts3.append(int(x))
            self.verts3.append(int(y))

    def draw_circle4(self, xorigin, yorigin):
        self.xorigin=xorigin
        self.yorigin=yorigin
        # global verts4
        self.verts4 = []
        # angle = 360 / max
        
        for i in range(self.max):
            angle_in_rad = ( self.angle * i) * (math.pi/180)
            cosine = math.cos(angle_in_rad) 
            sine = math.sin(angle_in_rad)
            
            x = cosine *self.radius - sine*self.radius + xorigin
            y = sine *self.radius + cosine*self.radius + yorigin
            
            self.verts4.append(int(x))
            self.verts4.append(int(y))

  
    # @window.event
    def on_draw(self):
        window.clear
        self.animSprite.draw()
        self.label.draw()
        
    global count
    count = 0

    def update(self,motion):

        self.animSprite.x+=5
        
        glPointSize(15)
        global count
        
        if(count < len(self.verts) - 1):

            glColor(0.0, 0.0, 1.0)
            glBegin(GL_POINTS)
            glVertex3f(self.verts[count], self.verts[count+1], 0)
            glEnd()
            count += 2

        if(count < len(self.verts1) - 1):
            
            glColor(1.0, 1.0, 1.0)
            glBegin(GL_POINTS)
            glVertex3f(self.verts1[count], self.verts1[count+1], 0)
            glEnd()
            count += 2
        
        if(count < len(self.verts2) - 1):

            glColor(1.0, 1.0, 0.0)
            glBegin(GL_POINTS)
            glVertex3f(self.verts2[count], self.verts2[count+1], 0)
            glEnd()
            count += 2

        if(count < len(self.verts3) - 1):

            glColor(0.0, 1.0, 0.0)
            glBegin(GL_POINTS)
            glVertex3f(self.verts3[count], self.verts3[count+1], 0)
            glEnd()
            count += 2

        if(count < len(self.verts4) - 1):

            glColor(1.0, 0.0, 0.0)
            glBegin(GL_POINTS)
            glVertex3f(self.verts4[count], self.verts4[count+1], 0)
            glEnd()
            count += 2
    
        # self.label.draw()


# pyglet.clock.tick(100)
window=Olyompics(900, 700, "Olyompic Rings Simulation",600,60)
window.draw_circle(230, 505)
window.draw_circle1(430, 505)
window.draw_circle2(330, 415)
window.draw_circle3(530, 415)
window.draw_circle4(630, 505)

pyglet.clock.schedule_interval(window.update, 0.11/120)

pyglet.app.run()