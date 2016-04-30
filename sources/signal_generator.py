import random

class Readings:
    def __init__ (self, limit=-1):
        self.limit = limit
        self._min = 0.0
        self._max = 1.0
    def __call__ (self):
        if(self.limit < 0):
            while True:
                yield random.gauss(self._min, self._max)
        else:
            count = 0
            while (count < self.limit):
                count += 1
                yield random.gauss(self._min, self._max)

