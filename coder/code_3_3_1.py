n = int(input())
a = list(map(int, input().split()))

b = 0
c = 0
d = 0
e = 0

for i in range(n):
    if a[i] == 100:
        b += 1
    if a[i] == 200:
        c += 1
    if a[i] == 300:
        d += 1
    if a[i] == 400:
        e += 1
print(str(b * e + c * d))
