def solve(l, r, A):
    if r - l ==  1:
        return A[l]
    m = (l+r)//2

    s1 = solve(l, m, A)
    s2 = solve(m, r, A)

    return s1 + s2

N = int(input())
A = list(map(int,input().split()))

answer = solve(0, N, A)
print(answer)
