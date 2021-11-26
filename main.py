import turtle as t
import random

# rgb = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
#        "SlateGray", "SeaGreen"]
# TODO: Random Color
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_random = (r, g, b)
    return color_random


tim = t.Turtle()
# tim.shape("turtle")
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
# angle = [45, 90, 135, 180, 225, 270, 315, 360]
# turn = ["right", "left"]
# pen_speed = 1
# tim.speed(1)
# tim.width(5)
# draw = 500
# while draw >= 0:
#     if pen_speed == 50 and tim.speed() < 10:
#         tim.speed(tim.speed() + 1)
#         pen_speed = 1
#     if random.choice(turn) == "right":
#         tim.right(random.randint(1, 360))
#     else:
#         tim.left(random.choice(angle))
#     tim.color(random_color())
#     tim.forward(20)
#     pen_speed += 1
#     draw -= 1
#     print(draw)

# TODO: Draw a Circle
tim.speed("fastest")
for n in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.right(5)

screen = t.Screen()
screen.exitonclick()
