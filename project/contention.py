#
# contention.py
# Project contention model
#

from math import floor, ceil
from nsga_ii import optimize
from random import gauss, random

BASE_DEV_RATE    = 0.01
BASE_SR_DEV_RATE = 0.01
SR_PROD_MULT     = 1.5
UNLEARNING_RATE  = 0.8

MILESTONE1a = 0.4
MILESTONE1b = 0.7
MILESTONE2  = 0.5

MAX_TIME   = 100
TIME_STEPS = 101
INIT_SD    = 0.1
MUTATE_SD  = 0.1

def run(sched):
  hist = []
  step_width = MAX_TIME / (TIME_STEPS - 1)

  # (t, proj1_seniors, proj1_tasks_by_sr, proj2_tasks_by_sr, proj1_complete,
  #  proj2_complete)
  state = (0, 0.5, 0.0, 0.0, 0.0, 0.0)
  hist.append(state)

  while state[4] < 1.0 or state[5] < 1.0:
    sr_dev_rate1 = BASE_SR_DEV_RATE + SR_PROD_MULT * state[2]
    sr_dev_rate2 = BASE_SR_DEV_RATE + SR_PROD_MULT * state[3]

    step = state[0] / step_width
    frac = (step - floor(step))
    d_proj1_seniors = frac * sched[floor(step)] + \
                      (1 - frac) * sched[ceil(step)]
    d_proj1_complete = BASE_DEV_RATE + sr_dev_rate1 * state[1]
    d_proj2_complete = BASE_DEV_RATE + sr_dev_rate2 * (1 - state[1])

    state = (state[0] + 1,
             min(max(state[1] + d_proj1_seniors, 0), 1),
             (state[2] + sr_dev_rate1 * state[1]) * UNLEARNING_RATE,
             (state[3] + sr_dev_rate2 * (1 - state[1])) * UNLEARNING_RATE,
             state[4] + d_proj1_complete,
             state[5] + d_proj2_complete,
             d_proj1_complete,
             d_proj2_complete)
    hist.append(state)

  return hist

def get_objectives(hist):
  for state in hist:
    if state[4] > MILESTONE1a:
      o1 = state[0] - (state[4] - MILESTONE1a) / state[6]
      break

  for state in hist:
    if state[4] > MILESTONE1b:
      o2 = state[0] - (state[4] - MILESTONE1b) / state[6]
      break

  for state in hist:
    if state[5] > MILESTONE2:
      o3 = state[0] - (state[5] - MILESTONE2) / state[7]
      break

  for state in hist:
    if state[4] >= 1.0:
      o4 = state[0] - (state[4] - 1.0) / state[6]
      break

  for state in hist:
    if state[5] >= 1.0:
      o5 = state[0] - (state[5] - 1.0) / state[7]
      break

  o6 = max(o4, o5)

  return (o1, o2, o3, o4, o5, o6)

# create a random schedule for initialization of optimization algorithms
def generate():
  return [gauss(0, INIT_SD) for _ in range(TIME_STEPS)]

def score(sched):
  return get_objectives(run(sched))

def combine(sched1, sched2):
  sched = [0.0] * TIME_STEPS

  # for each dimension, take the first value, second value or their average,
  # with equal probability
  for i in range(TIME_STEPS):
    x = random()

    if x < 1/3:
      sched[i] = sched1[i]
    elif x < 2/3:
      sched[i] = sched2[i]
    else:
      sched[i] = (sched1[i] + sched2[i]) / 2

    sched[i] = gauss(sched[i], MUTATE_SD)

  return sched

pop = optimize(generate, score, combine)
