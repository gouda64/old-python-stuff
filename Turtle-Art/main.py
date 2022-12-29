import turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.width(2)

ColorList = ['red', 'green', 'yellow', 'blue', 'lightblue']

def draw_art(d, angle, x, y):
  t.pendown()
  color = 0
  for i in range(1, 400):
    t.forward(d)
    t.left(angle)
    t.pencolor(ColorList[color])
    color = color + 1
    if color > 4:
      color = 0
    d = d - 1

#draw_art(150, 98, 0, 0)

def draw_rectangle(s, x, y):
  t.pendown()
  for i in range(4):
    t.forward(s)
    t.right(90)
    t.pencolor(ColorList[3])
  t.penup()

def draw_triangle(d, x, y):
  t.pendown()
  for i in range(3):
    t.forward(d)
    t.right(120)
    t.pencolor(ColorList[4])
  t.penup()

def draw_circle(r, x, y):
  t.pendown()
  for x in range(36):
    t.forward(r)
    t.right(10)
    t.pencolor(ColorList[0])
  t.penup()

def main():
  s = int(input("Choose a square size: "))
  d = int(input("Choose a triangle size: "))
  r = int(input("Choose a circle radius: "))
  for i in range(1, 400):
    draw_rectangle(s, 0, 0)
    draw_triangle(d, 0, 0)
    draw_circle(r, 0, 0)
    t.left(6)

if __name__ == "__main__":
  main()