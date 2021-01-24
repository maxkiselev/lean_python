from turtle import *
from math import pi, sin


def draw_polygons(polygon, line):
    angle = (((polygon - 2) * 180) / polygon) / 2
    left(angle)
    for i in range(polygon):
        left(360 / polygon)
        forward(line)
    right(angle)


def move_turtle():
    penup()
    forward(20)
    pendown()


shape('turtle')
color('green')
speed(5)
start_line = 20
r = 20

for i in range(3, start_line, 1):
    x = 2*r*sin(pi/i)
    draw_polygons(i, x)
    move_turtle()
    r += 20

mainloop()
