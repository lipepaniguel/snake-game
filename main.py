from turtle import Screen
from snake import Cobra

canvas = Screen()
celeste = Cobra()

canvas.listen()
canvas.onkeypress(celeste.sobe, 'w')
canvas.onkeypress(celeste.movimento, 'space')

canvas.exitonclick()
