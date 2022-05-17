
n,r = map(int, input().split())

def perm(n,r):
    ans = 1
    for i in range(r):
        ans = ans * (n-i)
    return ans

def com(n,r):
    bo = perm(r,r)
    si = perm(n,r)
    return(bo/si)

print(com(n,r))
