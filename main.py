from turtle import Screen
from snake import Cobra

canvas = Screen()
canvas.setup(400, 400)

celeste = Cobra()
celeste.shapesize(0.2, 0.2, 3)
celeste.shape('square')
celeste.penup()

celeste.speed(0)

wall = [380, -380]

canvas.listen()
canvas.onkeypress(celeste.sobe, 'w')
canvas.onkeypress(celeste.desce, 's')
canvas.onkeypress(celeste.direita, 'd')
canvas.onkeypress(celeste.esquerda, 'a')
canvas.onkeypress(celeste.pintar, 'space')

while True:
    celeste.movimento()
    print(celeste.xcor(), celeste.ycor())
    if celeste.xcor() in wall or celeste.ycor() in wall:
        print('bateu')
        break
