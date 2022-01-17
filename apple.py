from turtle import Turtle
import random


class Apple(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.resizemode('user')
        self.shapesize(0.3, 0.3)
        self.shape('circle')
        self.color('firebrick1')
        self.penup()
        self.speed(0)

    def nova_apple(self):
        self.hideturtle()
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        self.goto(x, y)
        self.showturtle()
