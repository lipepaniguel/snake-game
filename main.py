from turtle import Screen
from apple import maca, nova_apple
from snake import celeste
import random


def comecar():
    global continuar
    continuar = True


canvas = Screen()
canvas.title('Snake')
canvas.setup(400, 400)
canvas.screensize(370, 370)
canvas.bgcolor('black')

canvas.listen()
canvas.onkeypress(celeste.sobe, 'w')
canvas.onkeypress(celeste.desce, 's')
canvas.onkeypress(celeste.direita, 'd')
canvas.onkeypress(celeste.esquerda, 'a')

nova_apple()

comprimento = 0
score = 0

tamanho_tail = [0, 1]
tail = [0, 1, 2]

continuar = True

while continuar:
    print(tail)
    celeste.movimento()

    j = -1

    for i in range(len(tail) - 1):
        tail[j] = tail[j - 1]
        j -= 1

    tail[0] = (round(celeste.xcor()), round(celeste.ycor()))

    if (round(celeste.xcor()), round(celeste.ycor())) in tail[1:]:
        break

    if round(celeste.xcor()) >= 190 or round(celeste.xcor()) <= -190:
        break
    if round(celeste.ycor()) >= 190 or round(celeste.ycor()) <= -190:
        break

    if celeste.distance(maca) < 7:
        comprimento += 2
        score += 1
        tail.append(tamanho_tail[0])
        tail.append(tamanho_tail[1])

        nova_apple()

    celeste.rabo(comprimento)

canvas.exitonclick()
