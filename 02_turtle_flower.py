import turtle

turtle.shape('turtle')
turtle.color('red')
turtle.speed(10)

y = 45
for i in range(6):
    turtle.circle(50, 360)
    turtle.seth(y)
    y += 90

turtle.mainloop()

