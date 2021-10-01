from turtle import Screen
from snake import Cobra

canvas = Screen()
canvas.setup(400, 400)
canvas.screensize(370, 370)
canvas.bgcolor('black')

celeste = Cobra()

celeste.resizemode('user')
celeste.shapesize(0.2, 0.2, 3)
celeste.shape('square')
celeste.color('white')
celeste.penup()
celeste.speed(0)

canvas.listen()
canvas.onkeypress(celeste.sobe, 'w')
canvas.onkeypress(celeste.desce, 's')
canvas.onkeypress(celeste.direita, 'd')
canvas.onkeypress(celeste.esquerda, 'a')
canvas.onkeypress(celeste.teste_movimento, 'space')
canvas.onkeypress(celeste.teste_rabo, 'Return')

canvas.exitonclick()
