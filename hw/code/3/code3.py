from collections import defaultdict
from random import randrange
from Card import Deck
from PokerHand import PokerHand

#
# Exercise 8 (Birthday Paradox)
#
NUM_SAMPLES = 100000
NUM_STUDENTS = 23

def has_duplicates(l):
  return len(set(l)) < len(l)

n = 0

for _ in xrange(NUM_SAMPLES):
  if has_duplicates([randrange(365) for _ in range(NUM_STUDENTS)]):
    n += 1

print 'Estimate for birthday paradox with {} people:'.format(NUM_STUDENTS)
print '{}% chance of duplicate'.format(float(n) / NUM_SAMPLES * 100)

#
# Employee class
#
class Employee:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return '[{} ({} years old)]'.format(self.name, self.age)

  def __lt__(self, other):
    return self.age < other.age

#
# Exercise 6 (Poker)
#
NUM_TRIALS = 1000000

counts = defaultdict(int)

for _ in xrange(NUM_TRIALS):
  deck = Deck()
  deck.shuffle()
  hand = PokerHand()
  deck.move_cards(hand, 7)
  counts[hand.classify()] += 1

print
print 'Poker hands:'
for h in counts:
  print '  {}:{}{}'.format(h, ' ' * (20 - len(h)),
        float(counts[h]) / NUM_TRIALS)
