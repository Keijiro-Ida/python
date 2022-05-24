N, S = map(int, input().split())
A = list(map(int, input().split()))

result = 'No'
dp = [[False] * (S+1) for i in range(N+1)]
dp[0][0] = True

for i in range(0, N+1):
    for j in range(0, S+1):
        if dp[i-1][j] == True:
            dp[i][j] = True
            if j + A[i-1] <= S:
                dp[i][j+A[i-1]] = True

if dp[N][S]:
    result = 'Yes'
print(result)
