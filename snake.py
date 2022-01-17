from turtle import Turtle


class Cobra(Turtle):

    def __init__(self):
        super().__init__()
        self.resizemode('user')
        self.shapesize(0.3, 0.3)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed(0)

    def movimento(self):
        self.forward(2)

    def rabo(self, i):
        n = self.stamp() - i
        self.clearstamp(n)

    def sobe(self):
        self.setheading(90)

    def desce(self):
        self.setheading(270)

    def direita(self):
        self.setheading(0)

    def esquerda(self):
        self.setheading(180)
