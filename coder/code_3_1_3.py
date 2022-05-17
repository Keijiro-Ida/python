N = int(input())

Answer = []
limit = int(N**0.5)

for i in range(2, limit+1):
    if( N % i == 0):
        b = int( N / i)
        Answer.append(i)
        Answer.append(b)

print(*sorted(set(Answer)))
if len(Answer) == 0:
    print('Yes')
