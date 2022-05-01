N = int(input())
points =[]
for i in range(N):
    x,y = list(map(int, input().split()))
    points.append((x,y))

import math
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

ans = -1

for n1 in range(N):
    for n2 in range(N):
        ans = max(ans, distance(points[n1], points[n2]))

print(ans)
