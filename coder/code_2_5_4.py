def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input())
A = []
for i in range(2, n+1):
    if isprime(i) == True:
        A.append(i)

print(*A)
