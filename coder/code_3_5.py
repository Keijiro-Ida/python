import random

N =  10000
M = 0

for i in range(N):
    px = random.random()
    py = random.random()

    if px * px + py * py <= 1.0:
        M += 1

print("%.12f" % (4 * M / N))
