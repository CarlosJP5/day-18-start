from turtle import Turtle, Screen
import random

rgb = ["Red", "aquamarine1", "blue", "black", "green", "yellow", "maroon1", "tan2", "SlateBlue1", "DarkGoldenrod1",
       "light salmon", "LemonChiffon1", "khaki1", "OrangeRed", "seashell1", "wheat2"]
tim = Turtle()
tim.shape("turtle")
tim.color("Red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# Video 165

# TODO: Draw a square
# for n in range(4):
#     tim.forward(100)
#     tim.left(90)

# TODO: Draw a suspended line -> _ _ _ _ _ _
# for _ in range(10):
#     tim.pendown()
#     tim.forward(20)
#     tim.penup()
#     tim.forward(20)

# TODO: Draw different shapes, random color
# times = 10
# side = 3
# while times != 0:
#     tim.color(random.choice(rgb))
#     for _ in range(side):
#         tim.forward(100)
#         tim.right(360 / side)
#     side += 1
#     times -= 1

# TODO: Random walk, different colors, the thickness of the line grow and the draw speed up




screen = Screen()
screen.exitonclick()
