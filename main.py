from turtle import Turtle
from turtle import Screen
from apple import Apple
from snake import Cobra
import time

canvas = Screen()
canvas.title('Snake')
canvas.setup(400, 400)
canvas.screensize(370, 370)
canvas.bgcolor('black')

canvas.tracer(0)


def display():
    celeste.color('gray30')
    celeste.clearstamps()
    maca.hideturtle()
    pen.goto(0, 15)
    pen.write(f'Game Over', align='center', font=('Terminal', 30))
    pen.goto(0, -15)
    pen.write(f'Score: {score}', align='center', font=('Terminal', 14))


celeste = Cobra()

canvas.listen()
canvas.onkeypress(celeste.sobe, 'w')
canvas.onkeypress(celeste.desce, 's')
canvas.onkeypress(celeste.direita, 'd')
canvas.onkeypress(celeste.esquerda, 'a')

maca = Apple()

pen = Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)
pen.color('white')

comprimento = 0
score = 0

tamanho_tail = [0, 1]
tail = [0, 1, 2]

maca.nova_apple()

continuar = True

while continuar:

    time.sleep(0.01)
    canvas.update()
    celeste.movimento()

    j = -1

    for i in range(len(tail) - 1):
        tail[j] = tail[j - 1]
        j -= 1

    tail[0] = (round(celeste.xcor()), round(celeste.ycor()))

    if (round(celeste.xcor()), round(celeste.ycor())) in tail[3:]:
        display()
        continuar = False

    if round(celeste.xcor()) >= 189 or round(celeste.xcor()) <= -196:
        display()
        continuar = False

    if round(celeste.ycor()) >= 196 or round(celeste.ycor()) <= -187:
        display()
        continuar = False

    if celeste.distance(maca) < 7:
        comprimento += 2
        score += 1
        tail.append(tamanho_tail[0])
        tail.append(tamanho_tail[1])

        maca.nova_apple()

    celeste.rabo(comprimento)

canvas.update()
canvas.exitonclick()
