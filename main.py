from turtle import Turtle
from apple import maca, nova_apple
from snake import celeste
from tela import canvas

pen = Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)
pen.color('white')


def display():
    celeste.color('gray')
    celeste.clearstamps()
    maca.hideturtle()
    pen.goto(0, 15)
    pen.write(f'Game over.', align='center', font=('Terminal', 13))
    pen.goto(0, -15)
    pen.write(f'Score: {score}', align='center', font=('Terminal', 13))


comprimento = 0
score = 0

tamanho_tail = [0, 1]
tail = [0, 1, 2]

nova_apple()

continuar = True

while continuar:

    celeste.movimento()

    j = -1

    for i in range(len(tail) - 1):
        tail[j] = tail[j - 1]
        j -= 1

    tail[0] = (round(celeste.xcor()), round(celeste.ycor()))

    if (round(celeste.xcor()), round(celeste.ycor())) in tail[3:]:
        display()
        break

    if round(celeste.xcor()) >= 189 or round(celeste.xcor()) <= -196:
        display()
        break

    if round(celeste.ycor()) >= 196 or round(celeste.ycor()) <= -187:
        display()
        break

    if celeste.distance(maca) < 7:
        comprimento += 2
        score += 1
        tail.append(tamanho_tail[0])
        tail.append(tamanho_tail[1])

        nova_apple()

    celeste.rabo(comprimento)

canvas.exitonclick()
