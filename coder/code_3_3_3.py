
n,r = map(int, input().split())

fact_n = 1
for i in range(1, n+1):
    fact_n *= i


fact_r = 1
for i in range(1, r+1):
    fact_r *= i


fact_nr = 1
for i in range(1, n-r+1):
    fact_nr *= i

print(fact_n // (fact_r * fact_nr))
