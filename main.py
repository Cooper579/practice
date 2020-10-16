
import turtle as trtl

# The two "def" statements below define the code for create large and small stars
def star(size):
    circle_size = size
    for i in range(size):
        trtl.circle(circle_size,90)
        circle_size = circle_size - 1
    

#This code draws the stars in different sizes at different positions on the drawing
trtl.speed(0)
trtl.color("yellow")
trtl.penup()
trtl.setposition(-190,75)
trtl.pendown()
star(50)
trtl.penup()
trtl.setposition(15,190)
trtl.pendown()
star(45)
trtl.penup()
trtl.setposition(75,90)
trtl.pendown()
star(30)
trtl.penup()
trtl.setposition(-100,195)
trtl.pendown()
star(25)
trtl.penup()
trtl.setposition(-60,85)
trtl.pendown()
star(20)

def draw_axis():
  trtl.pendown()
  trtl.forward(200)
  trtl.backward(200)

draw_axis()

wn = trtl.Screen()
wn.mainloop()