from math import exp, sqrt
from random import random, randrange

ITERS = 200
TRIES = 1
STEPS = 10
EPS = 1e-10
SEARCH_DIST = 0.5

ranges = [(0, 10), (0, 10), (1, 5), (1, 6), (1, 5), (0, 10)]

def f1(x):
  return -(25 * (x[0] - 2)**2 + (x[1] - 2)**2 + (x[2] - 1)**2 * (x[3] - 4)**2 +
           (x[4] - 1)**2)

def f2(x):
  return sum(x_i**2 for x_i in x)

def valid(x):
  if x[0] + x[1] - 2 < -EPS:
    return False
  if 6 - x[0] - x[1] < -EPS:
    return False
  if 2 - x[1] + x[0] < -EPS:
    return False
  if 2 - x[0] + 3 * x[1] < -EPS:
    return False
  if 4 - (x[2] - 3)**2 - x[3] < -EPS:
    return False
  if (x[4] - 3)**3 + x[5] - 4 < -EPS:
    return False

  return True

# compute the limits for x[c] taking into account the constraints
def limits(x, c):
  if c == 0:
    return (max(0, 2 - x[1], x[1] - 2), min(10, 6 - x[1], 2 + 3 * x[1]))
  if c == 1:
    return (max(0, 2 - x[0], (x[0] - 2)/3.0), min(10, 6 - x[0], 2 + x[0]))
  if c == 2:
    return (max(1, 3 - sqrt(4 - x[3])), min(5, 3 + sqrt(4 - x[3])))
  if c == 3:
    return (0, min(6, 4 - (x[2] - 3)**2))
  if c == 4:
    return (max(1, 3 + ((4 - x[5])**(1.0/3) if 4 > x[5]
                                            else -(x[5] - 4)**(1.0/3))), 5)
  if c == 5:
    return (max(0, 4 - (x[4] - 3)**3), 10)

def energy(x):
  return f1(x) + f2(x)

e_best = 9e99
output = ''
bests = []

for i in xrange(TRIES):
  output += '!'
  x = [0] * 6

  while not valid(x):
    for i in range(6):
      x[i] = ranges[i][0] + random() * (ranges[i][1] - ranges[i][0])

  if energy(x) < e_best:
    e_best = energy(x)
    x_best = x
  bests.append(e_best)

  for j in xrange(ITERS):
    c = randrange(6)
    r = limits(x, c)
  
    if random() < 0.5:
      r = (max(r[0], x[c] - SEARCH_DIST), min(r[1], x[c] + SEARCH_DIST))
      x[c] = r[0] + random() * (r[1] - r[0])
      output += '?'
      bests.append(e_best)
    else:
      best_x = x[c]
      best_e = energy(x)
  
      for i in range(STEPS + 1):
        x[c] = r[0] + (float(i) / STEPS) * (r[1] - r[0])
  
        if energy(x) < best_e:
          best_e = energy(x)
          best_x = x[c]
          output += '+'
        else:
          output += '.'
        bests.append(e_best)
  
      x[c] = best_x
  
    if energy(x) < e_best:
      e_best = energy(x)
      x_best = x

print '!: restart'
print '+: improved one setting'
print '?: randomly changed one setting'
print '.: didn\'t change'
print

i = 0

while len(output):
  print '{}: {}  {}'.format(i, bests[i], output[:25])
  i += 25
  output = output[25:]

print 'x: {}'.format(','.join(str(x_i) for x_i in x_best))
print 'e: {}'.format(e_best)
