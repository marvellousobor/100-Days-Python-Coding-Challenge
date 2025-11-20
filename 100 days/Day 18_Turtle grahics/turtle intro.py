from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("red")
tim.speed(3)

for _ in range(15):
    tim.color("red")
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.color("black")
# CHALLENGE - 2


# CHALLENGE - 1
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# You can use 'import turtle as t' then tim = t

# import.heroes


# Keep this bit of code at the very bottom
screen = Screen()
screen.exitonclick()
