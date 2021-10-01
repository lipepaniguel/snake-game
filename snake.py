from turtle import Turtle


class Cobra(Turtle):

    def movimento(self):
        self.forward(3)

    def rabo(self, i):
        n = self.stamp() - i
        print(n)
        self.clearstamp(n)

    def sobe(self):
        self.setheading(90)

    def desce(self):
        self.setheading(270)

    def direita(self):
        self.setheading(0)

    def esquerda(self):
        self.setheading(180)

    def teste_movimento(self):
        self.forward(3)
        self.stamp()

    def teste_rabo(self):
        print(self.stamp())
        self.clearstamps(10)
