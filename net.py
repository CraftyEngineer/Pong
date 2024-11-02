from turtle import Turtle
class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.speed(0)
        self.pu()
        self.goto(0,-300)
        self.seth(90)
        self.pencolor("white")
        self.width(10)
        self.createnet()
    def createnet(self):
        while self.ycor()<310:
            self.pd()
            self.fd(20)
            self.pu()
            self.fd(30)