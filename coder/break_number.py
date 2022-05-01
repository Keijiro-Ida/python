n = int(input())

max = 0
ans = 1
for i in range(1,n+1):
    num = 0
    t = i
    while(t % 2 != 1):
        num += 1
        t = t//2

    if(max < num):
        max = num
        ans = i


print(ans)
