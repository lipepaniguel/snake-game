from turtle import Screen
from apple import nova_apple,  maca
from snake import celeste

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

i = 0
nova_apple()

while True:

    celeste.movimento()
    if celeste.xcor() >= 190 or celeste.xcor() <= -190:
        break
    if celeste.ycor() >= 190 or celeste.ycor() <= -190:
        break
    if celeste.distance(maca) < 6:
        i += 2
        nova_apple()

    celeste.rabo(i)

canvas.exitonclick()
