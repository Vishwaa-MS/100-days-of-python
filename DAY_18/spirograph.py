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


tim.speed('fastest')


def draw_spirographs(sides):
    for i in range(int(360 / sides)):
        tim.color(random_colour())
        current_heading = tim.heading()
        tim.circle(100)
        tim.setheading(current_heading + sides)


a = int(input('no of sides: '))


draw_spirographs(a)

screen = Screen()
screen.exitonclick()
