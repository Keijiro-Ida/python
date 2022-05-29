n, q = map(int, input().split())
A = list(map(int, input().split()))

B = [0 for _ in range(n)]
B[0] = A[0]
for i in range(1, n):
    B[i] = B[i-1] + A[i]

for i in range(q):
    l, r = map(int, input().split())
    if l == 1:
        print(B[r-1])
    else:
        print(B[r-1]-B[l-2])
