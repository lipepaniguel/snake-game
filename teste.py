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

variante_collider = 2
fator_rabo = 1
comprimento = 0
score = 0

tamanho_tail = [0]
tail = [0, 1, 2]

while continuar:

    celeste.movimento()

    j = -1

    for w in range(len(tail) - 1):
        tail[j] = tail[j - 1]
        j -= 1

    tail[0] = (round(celeste.xcor()), round(celeste.ycor()))

    # print(tail)

    if (round(celeste.xcor()), round(celeste.ycor())) in tail[1:]:
        print((round(celeste.xcor()), round(celeste.ycor())))
        print(len(tail))
        print(tail)
        continuar = False
        break

    if round(celeste.xcor()) >= 190 or round(celeste.xcor()) <= -190:
        break
    if round(celeste.ycor()) >= 190 or round(celeste.ycor()) <= -190:
        break
    if celeste.distance(maca) < 7:
        comprimento += 2
        score += variante_collider
        for x in range(variante_collider * fator_rabo):
            tail.append(x)

        nova_apple()

    celeste.rabo(comprimento)

canvas.exitonclick()
