import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


tim.speed(5)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b)
  return random_color

directions = [0, 45, 90, 135, 180, 225, 270, 315, 360]
tim.pensize(15)

for _ in range(200):
  tim.color(random_color())
  tim.forward(30)
  tim.setheading(random.choice(directions))