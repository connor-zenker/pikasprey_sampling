defs.py defines a function that returns the max of 1,000 draws from the binomial distribution, which is imported into test.ipynb for multithreading 
across 1,000,000 iterations, totaling our 1,000,000,000 trials.
Timing takes ~16.6s

Non-multithreaded, purely executing 1,000,000,000 draws from Binomial(231, 0.25)
Timing takes ~526.5s
