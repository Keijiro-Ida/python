n = int(input())
a = list(map(int, input().split()))

r, y, b = 0,0,0

for i in range(n):
    if a[i] == 1:
        r += 1
    if a[i] == 2:
        y += 1
    if a[i] == 3:
        b += 1

print(int(r * (r-1)/2 + y * (y-1)/2 + b *(b -1)/2))
