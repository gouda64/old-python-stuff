#Welcome to the Bethlehem Central High School Code Along
import turtle as t

print("Hi, my name is Erica.")

def build_house():
  size = 40*float(input("From a scale of 1 - 5 (1 the smallest, 5 the biggest), how big should the house be?"))
  building_color = input("What color should the building be?")
  roof_color = input("What color should the roof be?")
  door_color = input("What color should the door be?")
  handle = input("Do you want a door handle? (y/n)")
  window_color = input("What color should the window be?")
  garage_color = input("What color should the garage be?")
  garage_size = 40*float(input("From a scale of 1 - 5, how big should the garage be?"))
  t.speed(10)
  if handle == "y":
    handle = True
  else:
    handle = False
  if size > 200 or size < 40:
    print("Oops, you entered a size outside of the set range. Please try again!")
    size = 40*float(input("From a scale of 1 - 5, how big should the house be?"))
  if garage_size > 200 or garage_size < 40:
    print("Oops, you entered a garage size outside of the set range. Please try again!")
    garage_size = 40*float(input("From a scale of 1 - 5, how big should the garage be?"))
  for i in range(6):
    t.color(building_color)
    t.forward(size)
    t.left(90)
  t.right(60)
  for i in range(2):
    t.color(roof_color)
    t.forward(size)
    t.left(120)
  def make_window(window_color):
    t.pu()
    t.color(window_color)
    t.setposition(size*3/8, size*7/8)
    t.pd()
    for i in range(4):
      for i in range(5):
        t.right(90)
        t.forward(size/8)
      t.forward(size/8)
    t.pu()
    t.forward(size/2)
    t.pd()
    for i in range(4):
      for i in range(5):
        t.right(90)
        t.forward(size/8)
      t.forward(size/8)

  def make_door(door_color, handle):
    t.pu()
    t.setposition(size*3/8, 0)
    t.left(90)
    t.color(door_color)
    t.pd()
    t.forward(size/2)
    t.right(90)
    t.forward(size/4)
    t.right(90)
    t.forward(size/2)
    t.pu()
    if handle == True:
      t.right(90)
      t.forward(size/4)
      t.right(90)
      t.forward(size*15/64)
      t.right(90)
      t.forward(size/16)
      t.pd()
      t.circle(size/32)
    else:
      t.left(90)
  def make_garage(garage_color, garage_size):
    t.pu()
    t.setposition(size, 0)
    t.pd()
    for i in range(2):
      t.forward(garage_size)
      t.left(90)
      t.forward(garage_size*3/4)
      t.left(90)
    t.forward(garage_size/8)
    t.left(90)
    for i in range(4):
      for i in range(2):
        t.forward(garage_size*5/32)
        t.right(90)
        t.forward(garage_size*3/4)
        t.right(90)
      t.forward(garage_size*5/32)
  make_window(window_color)
  make_door(door_color, handle)
  make_garage(garage_color, garage_size)

build_house()

print(range(5))
for x in range(5):
	print(x)
# -------------- ignore everything above this line --------------

#Turtle Cheat Sheet
#t.forward(x) - use this to move forwards
#t.backward(x) - use to move backwards
#t.right(x) - use this to turn right by a specified number of degrees
#t.left(x) - use this to turn left by a specified number of degrees
#t.pu() - pen up
#t.pd() - pen down
#
