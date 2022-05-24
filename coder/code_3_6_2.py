from re import I


n = int(input())
a = list(map(int, input().split()))

for i in range(n-1):
    min_position = i
    min_value = a[i]
    for j in range(i+1, n):
        if a[j] < min_value:
            min_position = j
            min_value = a[j]
    a[i], a[min_position] = a[min_position], a[i]


for i in range(n):
    print(a[i])
