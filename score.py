from turtle import Turtle


class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.score = 0
        with open("records.txt", mode="r") as registro_record:
            conteudo_records = int(float(registro_record.read()))
        self.new_score = conteudo_records

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
            with open("records.txt", mode="w") as registro:
                registro.write(f'{self.new_score}')
            self.goto(0, -40)
            self.write(
                f'New Record: {self.new_score} !',
                align='center', font=('Terminal', 14)
                )

        self.score = 0
