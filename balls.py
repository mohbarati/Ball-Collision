from tkinter import *
import random

class Balls:
    color = ["red", "orange", "yellow", "green", "blue", "violet"]    
    v1x,v2x,v1y,v2y=0.1*random.randint(-10, 10),0.1*random.randint(-10, 10),0.1*random.randint(-10, 10),0.1*random.randint(-10, 10)
    def __init__(self, canvas,R,x1,y1,x2,y2):
        self.R=R
        self.x1 = x1
        self.y1=y1
        self.x2=x2
        self.y2 = y2
        self.canvas = canvas
        self.ball1 = canvas.create_oval(self.x1-self.R, self.y1-self.R,self.x1+self.R,self.y1+self.R, fill=random.choice(self.color))
        self.ball2 = canvas.create_oval(self.x2-self.R, self.y2-self.R,self.x2+self.R,self.y2+self.R, fill=random.choice(self.color))
        
        
    def callback(self):
        color=["red", "orange", "yellow", "green", "blue", "violet"] 
        self.AA=canvas.create_oval(self.x-10, self.y-10,self.x+10,self.y+10, fill=random.choice(color))
        self.vx,self.vy=0.5*random.randint(-10, 10),0.5*random.randint(-10, 10)
        canvas.move(self.AA, self.vx,self.vy)
        
        
        
    def move_balls(self):
        self.canvas.move(self.ball1, self.v1x,self.v1y)
        self.canvas.move(self.ball2, self.v2x,self.v2y)
        self.canvas.after(5, self.move_balls)
    def eventt(self):
        
        A=[(canvas.coords(self.ball1)[0]-canvas.coords(self.ball2)[0]),
           (canvas.coords(self.ball1)[1]-canvas.coords(self.ball2)[1])]
        if ((A[0])**2+(A[1])**2)**0.5<=2*self.R:
            self.v1x,self.v1y,self.v2x,self.v2y=self.v2x,self.v2y,self.v1x,self.v1y
            canvas.itemconfig(self.ball1,fill=random.choice(self.color)) 
            canvas.itemconfig(self.ball2,fill=random.choice(self.color))
        if canvas.coords(self.ball1)[0]<=0 or canvas.coords(self.ball1)[2]>=400:
            self.v1x=-self.v1x
        if canvas.coords(self.ball1)[1]<=0 or canvas.coords(self.ball1)[3]>=400:
            self.v1y=-self.v1y
        if canvas.coords(self.ball2)[0]<=0 or canvas.coords(self.ball2)[2]>=400:
            self.v2x=-self.v2x
        if canvas.coords(self.ball2)[1]<=0 or canvas.coords(self.ball2)[3]>=400:
            self.v2y=-self.v2y
        self.canvas.after(10,self.eventt)
# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(False,False)
canvas = Canvas(root, width = 400, height = 400)
canvas.bind("<Button-1>", Balls.callback)
canvas.pack()

# create two ball objects and animate them
ball = Balls(canvas ,20, 100, 200, 200, 300)
ball.move_balls()
ball.eventt()
root.mainloop()
