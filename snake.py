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
        self.comprimento = 0
        self.tamanho_rabo = [0, 1]
        self.tail = [0, 1, 2]

    def movimento(self):
        self.forward(2)

    def rabo(self, i):
        n = self.stamp() - i
        self.clearstamp(n)

    def novo_rabo(self):
        self.tail.append(self.tamanho_rabo[0])
        self.tail.append(self.tamanho_rabo[1])

    def sobe(self):
        self.setheading(90)

    def desce(self):
        self.setheading(270)

    def direita(self):
        self.setheading(0)

    def esquerda(self):
        self.setheading(180)

    def restart(self):
        self.comprimento = 0
        self.tamanho_rabo = [0, 1]
        self.tail = [0, 1, 2]
        self.goto(0, 0)
        self.color('white')
        self.showturtle()
