def GCD(A, B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A
        else:
            A = A % B
    if A >= 1:
        return A
    return B


n = int(input())
a = list(map(int, input().split()))

R = GCD(a[0], a[1])
for i in range(2, n):
    R = GCD(R, a[i])
print(R)
