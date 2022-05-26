x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
if dist < abs(r1-r2):
    print(1)
if dist==abs(r1-r2):
    print(2)
if dist>abs(r1-r2) and dist < abs(r1+r2):
    print(3)
if dist == abs(r1 + r2):
    print(4)
if dist > abs(r1 + r2):
    print(5)
