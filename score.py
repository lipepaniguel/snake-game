from turtle import Turtle


class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.score = 0
        self.new_score = 0

    def score_up(self):
        self.score += 1

    def display(self):
        self.goto(0, 15)
        self.write(f'Game Over', align='center', font=('Terminal', 30))
        self.goto(0, -15)
        self.write(
            f'Score: {self.score}', align='center', font=('Terminal', 14)
            )
        if self.score > self.new_score:
            self.new_score = self.score
            self.goto(0, -40)
            self.write(
                f'New Record: {self.new_score} !',
                align='center', font=('Terminal', 14)
                )
