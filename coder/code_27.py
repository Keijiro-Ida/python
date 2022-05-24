def MergeSort(A):

    if len(A)==1:
        return A

    m = len(A)//2
    A_dash = MergeSort(A[0:m])
    B_dash = MergeSort([A[m:len(A)]])

    c1 = 0
    c2 = 0
    C = []

    while (c1 < len(A_dash) or c2 < len(B_dash)):
        if c1 == len(A_dash):
            C.append(B_dash[c2])
            c2 += 1
        elif c2 == len(B_dash):
            C.append(A_dash[c1])
            c1 += 1
        else:
            if A_dash[c1] <= B_dash[c2]:
                C.append(A_dash[c1])
                c1 +=1
            else:
                C.append(B_dash[c2])
                c2 += 1


    return C


N = int(input())
A = list(map(int, input().split()))

Answer = MergeSort(A)
print(*Answer)
