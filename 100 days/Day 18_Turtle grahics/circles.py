import turtle as t
import random

tin = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tin.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tin.color(random_color())
        tin.circle(100)
        tin.setheading(tin.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
