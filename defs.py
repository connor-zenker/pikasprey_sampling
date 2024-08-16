import numpy as np

def f(n):
    draw = np.random.binomial(231, 0.25, 1000)
    maxD = max(draw)
    return maxD
