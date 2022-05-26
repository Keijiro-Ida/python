n = int(input())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
for i in range(n):
    x[i], y[i] = map(int, input().split())

Answer = 1000000000.0

for i in range(n):
    for j in range(i+1, n):
        dist = (((x[j]-x[i])**2 + (y[j]-y[i])**2)**0.5)
        Answer = min(Answer, dist)

print("%.12f" % Answer)
