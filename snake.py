from turtle import Turtle


class Cobra(Turtle):

    def movimento(self):
        self.forward(3)

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


celeste = Cobra()

celeste.resizemode('user')
celeste.shapesize(0.2, 0.2, 3)
celeste.shape('circle')
celeste.color('white')
celeste.penup()
celeste.speed(0)
