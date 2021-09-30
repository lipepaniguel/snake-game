from turtle import Screen
from snake import Cobra

canvas = Screen()
canvas.setup(800, 600)

celeste = Cobra()

celeste.speed(0)

wall = [290, -290]
wall2 = [390, -390]

canvas.listen()
canvas.onkeypress(celeste.sobe, 'w')
canvas.onkeypress(celeste.desce, 's')
canvas.onkeypress(celeste.direita, 'd')
canvas.onkeypress(celeste.esquerda, 'a')

while True:
    celeste.movimento()
    if celeste.xcor() in wall2 or celeste.ycor() in wall:
        print('bateu')
        break
