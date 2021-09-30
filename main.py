from turtle import Turtle, Screen
import snake as sk

canvas = Screen()
canvas.setup(800, 600)
sk.celeste.speed(1)

wall = [300, -300]

canvas.listen()
canvas.onkeypress(sk.sobe, 'w')
canvas.onkeypress(sk.desce, 's')
canvas.onkeypress(sk.direita, 'd')
canvas.onkeypress(sk.esquerda, 'a')

while True:
    sk.movimento()
    if sk.celeste.xcor() in wall or sk.celeste.ycor() in wall:
        break

canvas.exitonclick()
