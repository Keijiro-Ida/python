n = int(input())
a = list(map(int, input().split()))

cnt = [0 for i in range(100000)]
for i in range(n):
    cnt[a[i]] += 1


sum = 0
for i in range(1, 50000):
    sum += cnt[i] * cnt[100000-i]

sum += cnt[50000] * (cnt[50000]-1) //2

print(sum)
