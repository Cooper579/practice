import turtle as trtl

#defines house
#takes two parameters
#size of the house and pensize
def house(size,pen):
  #turns the pen color to blue and the pen size to what was set
  trtl.color("royalblue")
  trtl.pensize(pen)
  trtl.setheading(-90)
  trtl.pendown()
  #makes the bottom of the house
  for i in range(3):
    trtl.forward(size*1.25)
    trtl.left(90)
  #makes the triangles
  trtl.color("steelblue")
  trtl.penup()
  trtl.right(90)
  trtl.forward(size*2)
  trtl.left(90)
  trtl.forward((size*1.25)/2)
  trtl.pendown()
  trtl.circle(size,360,3)
  #makes a door
  trtl.color("black")
  trtl.pensize(pen/1.5)
  trtl.penup()
  trtl.left(90)
  trtl.forward(size*3.5)
  trtl.left(180)
  trtl.pendown()
  trtl.forward(size/1.5)


for i in range(3):
  house(10,15)
  trtl.penup()
  trtl.setheading(0)
  trtl.forward(20)
  trtl.setheading(90)
  trtl.forward(10)
  trtl.setheading(0)

wn = trtl.Screen()
wn.mainloop()