N, K = map(int, input().split())
A = list(map(int, input().split()))
# N, K = 4, 10
# A = [1, 2, 3, 4]


def check(sec):
    sum = 0
    for i in range(N):
        sum += sec//A[i]

    return sum


left = 1
right = 10**9
ans = 0

# left<rightで固定しよう
while (left < right):
    mid = (left+right)//2
    canditate = check(mid)
    # 値が同一が複数回存在する
    if canditate < K:
        left = mid+1
        ans = mid+1
    else:
        right = mid
        # ans = mid

print(ans)
