
# Copia aquí la definición del nodo que resuelve
# el VPL anterior!
from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room = room

    def estimate(self, items):
        x = 0 
        n = self.index - 1
        for i in items[self.index - 1:]:
            x = x + i.value
        return x
