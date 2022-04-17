N,A,B = map(int,input().split())

ans = 0

def find_sum(n):
    sum = 0
    while n > 0:
        sum += n %10
        n = n//10
    return sum

for i in range(1,N+1):
    sum2 = find_sum(i)

    if A <= sum2 <= B:
        ans+=i
print(ans)
