#! /usr/bin/env python

import turtle
import flower

num = raw_input("Enter the number of petals: ")
turtle.penup()
turtle.setposition(-90,250)
turtle.pendown()
turtle.pencolor("purple")
turtle.write("Sarah", True, align="center", font = ("Arial",50,"normal"))

turtle.penup()
turtle.setposition(0,-150)
turtle.pendown()
turtle.left(90)
turtle.pencolor("green")
turtle.forward(150)


for i in range(int(num)):
    flower.square("red",60)
    turtle.left(360/int(num))

turtle.mainloop()
