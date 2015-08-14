import random
import bisect

class WeightedRandomItemSelector(object):
    """Weighted Random Item Selector
        We keep two arrays, one for holding an incrementing total of weights, and another for holding the items that corresponds to it
        Selection: O(log n) + overhead for random.random() (where n is number of itmes in array)
        Insertion: O(1)
        Improvised version of:
        http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/ """
    def __init__(self):
        self.totals = []
        self.items = []
        self.running_total = 0 
    def add(self, item, weight):
        # running_total continues to increase, which means self.totals will always be in sorted order
        # which allows us to use bisect
        self.running_total += weight
        self.totals.append(self.running_total)
        self.items.append(item) 
    def next(self):
        rnd = random.random() * self.totals[-1]
        idx = bisect.bisect_right(self.totals, rnd)
        return self.items[idx]
