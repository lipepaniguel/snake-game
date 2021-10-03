from turtle import Screen
from apple import maca, nova_apple
from snake import celeste
import random

continuar = True


def comecar():
    global continuar
    continuar = True


canvas = Screen()
canvas.title('Snake')
canvas.setup(400, 400)
canvas.screensize(370, 370)
canvas.bgcolor('black')

nova_apple()

canvas.listen()
canvas.onkeypress(celeste.sobe, 'w')
canvas.onkeypress(celeste.desce, 's')
canvas.onkeypress(celeste.direita, 'd')
canvas.onkeypress(celeste.esquerda, 'a')
# canvas.onkeypress(celeste.movimento, 'space')

variante_collider = 3

comprimento = 0
score = 0

tamanho_tail = [0]
tail = [0, 1, 2]

while continuar:

    celeste.movimento()
    ultimo_rabo = celeste.pos()
    for numero in range(variante_collider):

        j = -1

        for w in range(len(tail) - 1):
            tail[j] = tail[j - 1]
            j -= 1

    tail[0] = (celeste.xcor(), celeste.ycor())
    tail[1] = (celeste.xcor(), celeste.ycor() - 1)
    tail[2] = (celeste.xcor() - 1, celeste.ycor())
    # tail[3] = (celeste.xcor(), celeste.ycor() - 1.5)
    # tail[4] = (celeste.xcor() - 1.5, celeste.ycor())

    # print(tail)

    if celeste.pos() in tail[3:]:
        continuar = False
        break

    if celeste.xcor() >= 190 or celeste.xcor() <= -190:
        break
    if celeste.ycor() >= 190 or celeste.ycor() <= -190:
        break
    if celeste.distance(maca) < 7:
        comprimento += 2
        score += variante_collider
        for x in range(score):
            tail.append(x)

        nova_apple()

    celeste.rabo(comprimento)

canvas.exitonclick()
