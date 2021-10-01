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
score = 0
nova_apple()
tamanho_tail = [0]
tail = [0]
ultimo_rabo = []


while True:

    celeste.movimento()
    ultimo_rabo = celeste.pos()

    j = -1

    for i in range(len(tail) - 1):
        tail[j] = tail[j - 1]
        j -= 1

    tail[0] = ultimo_rabo

    if len(tail) > 0:
        print(tail[1:])
        if celeste.pos() in tail[1:]:
            break

    if celeste.xcor() >= 190 or celeste.xcor() <= -190:
        break
    if celeste.ycor() >= 190 or celeste.ycor() <= -190:
        break
    if celeste.distance(maca) < 6:
        i += 2
        score += 1
        tail.append(score)
        nova_apple()

    celeste.rabo(i)

canvas.exitonclick()
