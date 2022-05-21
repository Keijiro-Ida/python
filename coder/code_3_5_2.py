import random

N = 1000000
M = 0

for i in range(N):
    px = 6.0 * random.random()
    py = 9.0 * random.random()

    dist_33 = ((px-3.0) * (px-3.0) + (py-3.0)+(py-3.0))**0.5
    dist_37 = ((px-3.0) * (px-3.0) + (py-7.0)+(py-7.0))**0.5

    if (dist_33.real <= 3.0 or dist_37.real <= 2.0):
        M += 1
print(M)
