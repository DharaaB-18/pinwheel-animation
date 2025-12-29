import turtle
import time

window = turtle.Screen()
window.title("Pinwheel")

pinwheel = turtle.Turtle()
pinwheel.speed(10)
window.bgcolor("black")

colors = ["violet","indigo","blue","green","yellow","orange","red","pink"]

pinwheel.right(30)

def y():
  for c in colors:
    time.sleep(1)
    pinwheel.color(c)
    pinwheel.forward(80)
    pinwheel.left(90)
    pinwheel.forward(80)
    pinwheel.left(135)
    pinwheel.forward(113)
    pinwheel.left(180)

y()

pinwheel.color("grey")
pinwheel.penup()
pinwheel.right(60)
pinwheel.forward(95)
pinwheel.pendown()
pinwheel.width(3)
pinwheel.forward(200)

turtle.done()
