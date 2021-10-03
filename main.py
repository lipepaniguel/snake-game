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

comprimento = 0
score = 0

tamanho_tail = [0]
tail = [0]
ultimo_rabo = []


while continuar:

    celeste.movimento()
    ultimo_rabo = celeste.pos()

    j = -1

    for i in range(len(tail) - 1):
        tail[j] = tail[j - 1]
        j -= 1

    tail[0] = ultimo_rabo

    if celeste.pos() in tail[1:]:
        continuar = False
        break

    # if len(tail) > 0:
    #     for _ in tail[1:]:

    #         if celeste.distance(_) < 3:
    #             continuar = False
    #             break

    if celeste.xcor() >= 190 or celeste.xcor() <= -190:
        break
    if celeste.ycor() >= 190 or celeste.ycor() <= -190:
        break
    if celeste.distance(maca) < 7:
        comprimento += 2
        score += 1
        tail.append(score)

        nova_apple()

    celeste.rabo(comprimento)

canvas.exitonclick()
