import random
import math

count = 0  # Counter of the num. of developed nodes.

'''
Simulates the maximum players alpha-beta pruning algorithm
bf=the branching factor
d=the trees depth
a=alpha
b=beta
'''


def a_b_max(bf, depth, a, b):
    global count
    count += 1
    if depth == 0:
        return random.randrange(1, 1000000000)
    v = float("-inf")
    for i in range(bf):
        tmp = a_b_min(bf, depth - 1, a, b)
        if tmp >= b:
            return tmp
        if tmp > a:
            a = tmp
        if tmp > v:
            v = tmp
    return v


def a_b_min(bf, depth, a, b):
    """
    Your code comes here.
    Implement the minimum player in alpha-beta pruning
    """
    global count
    count += 1
    if depth == 0:
        return random.randrange(1, 1000000000)
    v = float("inf")
    for i in range(bf):
        tmp = a_b_max(bf, depth - 1, a, b)
        if tmp < a:
            return tmp
        if tmp > a:
            a = tmp
        if tmp > v:
            v = tmp
    return v


def simulate(b, d):
    a_b_max(b, d, float("-inf"), float("inf"))


def calc_effective_d(b):
    """
    Your code comes here.
    calculate the effective height of the developed tree
    from b (the branching factor) and count(the number of nodes developed).
    """


d = 16  # Depth of the tree
b = 4  # Branching factor
simulate(b, d)
print(count)
print(calc_effective_d(b))
