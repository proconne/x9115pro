"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *
from collections import defaultdict


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = defaultdict(int)
        for card in self.cards:
            self.suits[card.suit] += 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = defaultdict(int)
        for card in self.cards:
            self.ranks[card.rank] += 1

    def has_straightflush(self):
        suit = None
        self.suit_hist()
        for s in self.suits:
            if self.suits[s] >= 5:
                suit = s
                break
        if not suit: return False
        ranks = range(1, 14) + [1]
        for i in range(10):
            if all(any(c.suit == suit and c.rank == r for c in self.cards)
                   for r in ranks[i:i+5]):
                return True
        return False

    def has_quads(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_fullhouse(self):
        exclude = -1
        self.rank_hist()
        for rank in self.ranks:
            if self.ranks[rank] >= 3:
                exclude = rank
                break
        if exclude == -1: return False
        for rank in self.ranks:
            if rank != exclude and self.ranks[rank] >= 2:
                return True
        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_straight(self):
        self.rank_hist()
        ranks = range(1, 14) + [1]
        for i in range(0, 10):
            r = ranks[i:i+5]
            if all(self.ranks[r_i] > 0 for r_i in r):
                return True
        return False

    def has_trips(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_twopair(self):
        exclude = -1
        self.rank_hist()
        for rank in self.ranks:
            if self.ranks[rank] >= 2:
                exclude = rank
                break
        if exclude == -1: return False
        for rank in self.ranks:
            if rank != exclude and self.ranks[rank] >= 2:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def classify(self):
        if self.has_straightflush():
            return 'straight flush'
        if self.has_quads():
            return 'four of a kind'
        if self.has_fullhouse():
            return 'full house'
        if self.has_flush():
            return 'flush'
        if self.has_straight():
            return 'straight'
        if self.has_trips():
            return 'three of a kind'
        if self.has_twopair():
            return 'two pair'
        if self.has_pair():
            return 'pair'
	return 'high card'

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print hand.has_flush()
        print ''

