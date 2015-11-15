from math import atan, asin, pi, sin
from polygon import arc
from swampy.TurtleWorld import Turtle, TurtleWorld, pu, pd, fd, lt, rt

# t: turtle
# n: number of petals
# rf: flower radius
# re: radius of edge arcs
def flower(t, n, rf, re):
  angle = asin(0.5 * float(rf) / re) * 180 / pi
  rt(t, angle)

  for _ in range(n):
    arc(t, re, angle * 2)
    lt(t, 180 - angle * 2)
    arc(t, re, angle * 2)
    lt(t, 180 - angle * 2 + 360 / n)

# wrapper function that sets up a world and draws a flower
# arguments are same as flower
def drawFlower(n, rf, re):
  world = TurtleWorld()
  t = Turtle()
  t.delay = 0.001
  flower(t, n, rf, re)

# t: turtle
# sides: number of sides
# radius: length of sides coming from the center
def pie(t, sides, radius):
  angle1 = 360.0 / sides
  angle2 = (180.0 - angle1) / 2
  print angle1
  print angle2
  rt(t, angle1 / 2)

  for _ in range(sides):
    fd(t, radius)
    lt(t, 180 - angle2)
    fd(t, 2 * radius * sin(pi / 180 * angle1 / 2))
    lt(t, 180 - angle2)
    fd(t, radius)
    rt(t, 180)

# wrapper function that sets up a world and draws a pie
# arguments are same as pie
def drawPie(sides, radius):
  world = TurtleWorld()
  t = Turtle()
  t.delay = 0.001
  pie(t, sides, radius)
