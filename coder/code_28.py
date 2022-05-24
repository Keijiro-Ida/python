from tkinter import N


n = int(input())
h = list(map(int, input().split()))

dp = [None] * n
dp[0] = 0

for i in range(n):
    if i == 1:
        dp[1] = abs(h[i] - h[i-1])
    if i >= 2:
        v1 = dp[i-1] + abs(h[i]-h[i-1])
        v2 = dp[i-2] + abs(h[i]-h[i-2])

        dp[i] = min(v1, v2)

print(dp[n-1])
