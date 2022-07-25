import turtle as t
import random

t.colormode(255)
t.setworldcoordinates(0, 0, 460, 460)
color_list = [(225, 237, 231), (237, 232, 217), (141, 176, 206), (25, 32, 48), (27, 107, 157), (239, 226, 236),
              (208, 161, 112), (230, 211, 94), (132, 31, 65), (6, 162, 196), (181, 45, 83), (217, 61, 87),
              (194, 130, 169), (54, 167, 116)]

bob = t.Turtle()
bob.hideturtle()
bob.penup()
bob.speed("fastest")


def draw_dot_line():
    for col in range(10):
        bob.dot(20, random.choice(color_list))
        bob.forward(50)


def go_next_line():
    bob.left(90)
    bob.forward(50)
    bob.left(90)
    bob.forward(500)
    bob.right(180)


for row in range(10):
    draw_dot_line()
    go_next_line()


screen = t.Screen()
screen.exitonclick()
