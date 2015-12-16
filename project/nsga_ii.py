#
# nsga-ii.py
#

from random import randrange, shuffle

POP_SIZE = 500
ITERS    = 1000

goals = [(0, 0, 0, 0, 0, -1), (0, 0, 0, 0, -1, 0), (0, 0, 0, -1, -1, 0), 
         (-1, -1, 0, 0, -1, 0), (-1, -1, -1, -1, -1, -1)]
best = [()] * len(goals)
best_obj = [-9e99] * len(goals)

def dominates(s1, s2):
  return all(s1_i <= s2_i for (s1_i, s2_i) in zip(s1, s2))

def get_nondom_lvls(pop):
  counts = {i: 0 for i in range(len(pop))}
  dom_by = {i: set() for i in range(len(pop))}
  lvls = []
  remaining = set(i for i in range(len(pop)))

  for i in range(len(pop) - 1):
    for j in range(i + 1, len(pop)):
      if dominates(pop[i][0], pop[j][0]):
        counts[j] += 1
        dom_by[i].add(j)
      elif dominates(pop[j][0], pop[i][0]):
        counts[i] += 1
        dom_by[j].add(i)

  while remaining:
    next_group = set()

    for i in set(remaining):
      if counts[i] == 0:
        next_group.add(i)
        remaining.remove(i)

    lvls.append([])

    for i in next_group:
      lvls[-1].append(i)

      for j in dom_by[i]:
        counts[j] -= 1

  return lvls

def optimize(generate, score, combine):
  pop = []

  for _ in range(POP_SIZE):
    x = generate()
    pop.append((x, score(x)))

  for iter in range(ITERS):
    if iter % 10 == 0:
      print('Iteration {}/{}:'.format(iter, ITERS))

    for i in range(len(goals)):
      for x in pop:
        obj = sum(goals[i][j] * x[1][j] for j in range(len(goals[i])))

        if obj > best_obj[i]:
          best_obj[i] = obj
          best[i] = x[0]
          print('  Found new best for goal {}'.format(i))

    for _ in range(POP_SIZE):
      i = randrange(POP_SIZE)
      j = randrange(POP_SIZE)
      x = combine(pop[i][0], pop[j][0])
      pop.append((x, score(x)))

    lvls = get_nondom_lvls(pop)
    new_pop = []

    while len(new_pop) + len(lvls[0]) <= POP_SIZE:
      new_pop.extend(pop[i] for i in lvls[0])
      lvls = lvls[1:]

    more_needed = POP_SIZE - len(new_pop)
    consider = lvls[0]

    if more_needed:
      ii = list(range(len(pop)))
      dist = {i: 0 for i in ii}

      for j in range(len(pop[0][0])):
        f_max = max(p[0][j] for p in pop)
        f_min = min(p[0][j] for p in pop)

        ii.sort(key=lambda i: pop[i][0][j])
        dist[ii[0]] = 9e99
        dist[ii[-1]] = 9e99

        for i in range(1, len(pop) - 1):
          dist[ii[i]] += (pop[ii[i + 1]][0][j] - pop[ii[i - 1]][0][j]) / \
                         (f_max - f_min)

      consider.sort(key=lambda i: dist[i])
      new_pop.extend(pop[i] for i in consider[-more_needed:])

    pop = new_pop

  print(' '.join(str(x) for x in best_obj))
  return best
