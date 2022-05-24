def GCD(A, B):
    if B == 0:
        return A
    return GCD(B, A % B)

A, B = map(int, input().split())
print(GCD(A, B))
