import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_c = (r, g, b)
    return random_c


directions = [0, 90, 180, 270]

for _ in range(200):
    tim.pensize(5)
    tim.speed('fastest')
    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
