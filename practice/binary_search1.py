N, X = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = N-1
ans = 0
while (left <= right):
    mid = (left+right)//2
    if A[mid] == X:
        ans = mid
        break
    elif A[mid] < X:
        left = mid+1
    else:
        right = mid-1

print(ans+1)
