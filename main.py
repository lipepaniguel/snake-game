from turtle import Screen
from snake import Cobra

canvas = Screen()
canvas.setup(400, 400)
canvas.screensize(370, 370)
celeste = Cobra()
celeste.resizemode('user')
celeste.shapesize(0.2, 0.2, 3)
celeste.shape('square')
celeste.penup()
celeste.speed(0)

canvas.listen()
canvas.onkeypress(celeste.sobe, 'w')
canvas.onkeypress(celeste.desce, 's')
canvas.onkeypress(celeste.direita, 'd')
canvas.onkeypress(celeste.esquerda, 'a')
canvas.onkeypress(celeste.pintar, 'space')

while True:
    celeste.movimento()
    if celeste.xcor() >= 180 or celeste.xcor() <= -180:
        print('bateu')
        break
    if celeste.ycor() >= 180 or celeste.ycor() <= -180:
        print('bateu')
        break

canvas.exitonclick()
