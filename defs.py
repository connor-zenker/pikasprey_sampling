import numpy as np

def f(n):
    maxD = 0
    for i in range(0,1000):
        draw = np.random.binomial(231, 0.25)
    if draw > maxD:
        maxD = draw
    return maxD