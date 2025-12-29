import ColabTurtlePlus.Turtle as t

import time

t.initializeTurtle()
t.speed(10)
t.bgcolor("black")

colors = ["violet","indigo","blue","green","yellow","orange","red","pink"]

t.right(30)

def y():
  for c in colors:
    time.sleep(1)
    t.color(c)
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(135)
    t.forward(113)
    t.left(180)

y()

t.color("grey")
t.penup()
t.right(60)
t.forward(95)
t.pendown()
t.width(3)
t.forward(200)
