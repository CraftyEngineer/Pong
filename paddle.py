from turtle import Turtle
PADDLE1_START=(380,0)
PADDLE2_START=(-380,0)
class Paddle(Turtle):
    def __init__(self,x_cor, y_cor):
        super().__init__()
        self.segments = []
        self.x_cor=x_cor
        self.y_cor=y_cor
        self.createpaddle(self.x_cor,  self.y_cor)
    
    def createpaddle(self,x_cor, y_cor):
        self.seth(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(x_cor, y_cor)
    
    def go_up(self):
        self.forward(20)
    
    def go_down(self):
        self.backward(20)
    
   



            
