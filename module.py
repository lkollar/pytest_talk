
import random

class DivError(Exception):
    ERROR = 100

def add(x, y):
    return x + y

def div(x, y):
    if y == 0:
        raise DivError()

    return x / y

def add_random(x):
    n = random.randint(0, 100)
    return x + n

def add_random_2(rand_func, x):
    n = rand_func(0, 100)
    return x + n


class Adder(object):
    def __init__(self, x):
        self.x = x

    def add(self, y):
        return self.x + y

