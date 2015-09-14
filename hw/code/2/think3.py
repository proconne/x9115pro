#
# think3.py
#

def right_justify(string):
  print ' ' * (70 - len(string)) + string

def do_twice(f, x):
  f(x)
  f(x)

def print_twice(string):
  print string
  print string

def do_four(f, x):
  do_twice(f, x)
  do_twice(f, x)

def print_horiz(size):
  print '+' + (' -' * 4 + ' +') * size

def print_verts(size):
  for i in range(4):
    print '/' + (' ' * 9 + '/') * size

def print_grid(size):
  print_horiz(size)

  for i in range(size):
    print_verts(size)
    print_horiz(size)

print_grid_2 = lambda: print_grid(2)
print_grid_4 = lambda: print_grid(4)

print '3.3:'
right_justify('hello')
print

print '3.4:'
do_twice(print_twice, 'spam')
print

print '3.5:'
print_grid_2()
print
print_grid_4()
