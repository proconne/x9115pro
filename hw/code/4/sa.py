from math import exp
from random import gauss, random

MUTATE_SD = 2.0
ITERS = 1000

def f1(x):
  return x**2

def f2(x):
  return (x - 2)**2

def energy(x):
  return (f1(x) + f2(x) - 2.0) / 2500.0

x = 0.0
e = energy(x)
x_best = x
e_best = e
line = '!'

for i in xrange(ITERS):
  x_new = gauss(x, MUTATE_SD)
  e_new = energy(x_new)

  if e_new < e:
    line += '+'
    x = x_new
    e = e_new
  elif random() > exp((e - e_new) * ITERS / (float(i) + 1)):
    line += '?'
    x = x_new
    e = e_new
  else:
    line += '.'

  if e < e_best:
    e_best = e
    x_best = x

  if len(line) == 25:
    print i - 23, ':{}'.format(e_best), line
    line = ''

print 'x:', x_best
print 'e:', e_best
