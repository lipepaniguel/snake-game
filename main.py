from turtle import Screen
from snake import Cobra

canvas = Screen()
canvas.title('Snake')
canvas.setup(400, 400)
canvas.screensize(370, 370)
canvas.bgcolor('black')

celeste = Cobra()

celeste.resizemode('user')
celeste.shapesize(0.2, 0.2, 3)
celeste.shape('circle')
celeste.color('white')
celeste.penup()
celeste.speed(0)


def aumenta_rabo():
    global i
    i += 2


canvas.listen()
canvas.onkeypress(celeste.sobe, 'w')
canvas.onkeypress(celeste.desce, 's')
canvas.onkeypress(celeste.direita, 'd')
canvas.onkeypress(celeste.esquerda, 'a')
canvas.onkeypress(aumenta_rabo, 'space')

i = 0

while True:

    celeste.movimento()
    if celeste.xcor() >= 180 or celeste.xcor() <= -180:
        print('bateu')
        break
    if celeste.ycor() >= 180 or celeste.ycor() <= -180:
        print('bateu')
        break
    celeste.rabo(i)

canvas.exitonclick()
