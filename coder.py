A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for i in range(0, A+1):
    for j in range(0, B+1):
        for k in range(0, C+1):
            ttl = 0
            ttl = 500 * i + 100 * j +  50 * k
            print(ttl)
            if(ttl ==X):
                ans = ans +1

print(ans)
