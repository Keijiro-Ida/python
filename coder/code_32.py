N, X = map(int, input().split())
A =list(map(int, input().split()))

A.sort()

answer = 'No'
left, right = 0, N-1

while left <= right:
    mid = (left+right) // 2
    if A[mid] == X:
        answer = 'Yes'
        break
    if A[mid] < X:
        left = mid + 1
    if A[mid] > X:
        right = mid-1

print(answer)
