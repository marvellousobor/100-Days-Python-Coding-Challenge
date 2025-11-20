import turtle as t
from turtle import Screen
import random

tin = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tin.pensize(15)
tin.speed("fastest")

for _ in range(200):
    tin.color(random_color())
    tin.forward(30)
    tin.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
