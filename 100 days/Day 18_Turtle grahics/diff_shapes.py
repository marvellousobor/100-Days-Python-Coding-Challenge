from turtle import Turtle, Screen
import random

pol = Turtle()

pol.shape("arrow")

colours = ["CornflowerBlue", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        pol.forward(100)
        pol.right(angle)


for shape_side_n in range(3, 11):
    pol.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
