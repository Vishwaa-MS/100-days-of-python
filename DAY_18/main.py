from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def shapes_in_screen(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    tim.color(random.choice(colours))
    shapes_in_screen(i)

screen = Screen()
screen.exitonclick()
