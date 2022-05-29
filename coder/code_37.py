def cross(ax, ay, bx, by):
    return ax*by - ay*bx

X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())
X4, Y4 = map(int, input().split())

ans1 = cross(X2-X1, Y2-Y1, X3-X1,Y3-Y1)
ans2 = cross(X2-X1, Y2-Y1, X4-X1, Y4-Y1)
ans3 = cross(X4-X3, Y4-Y3, X1-X3, Y1-Y3)
ans4 = cross(X4-X3, Y4-Y3, X2-X3, Y2-Y3)

if ans1 == 0 and ans2==0 and ans3==0 and ans4==0:
    A = (X1, Y1)
    B = (X2, Y2)
    C = (X3, Y3)
    D = (X4, Y4)
    if A > B:
        tmp = B
        B = A
        A = tmp
    if C > D:
        tmp = D
        D = C
        C = tmp
    if max(A, C) <= min(B, D):
        print('Yes')
    else:
        print('No')

else:
    IsAB = False
    IsCD = False
    if ans1 >=0 and ans2 <= 0:
        IsAB = True
    if ans1 <=0 and ans2 >= 0:
        IsAB = True
    if ans3 >= 0 and ans4 <= 0:
        IsCD = True
    if ans3 <= 0 and ans4 >= 0:
        IsCD = True
    if IsAB == True and IsCD == True:
        print('Yes')
    else:
        print('No')
