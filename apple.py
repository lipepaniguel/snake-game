from snake import celeste
import random

maca = celeste.clone()
maca.color('firebrick1')


def nova_apple():
    maca.hideturtle()
    x = random.randint(-180, 180)
    y = random.randint(-180, 180)
    maca.goto(x, y)
    maca.showturtle()
