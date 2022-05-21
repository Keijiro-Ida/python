n = int(input())
ans = 0
for i in range(n):
    ans += n / (n -i)

print(ans)
