N, K = map(int, input().split())
A = list(map(int, input().split()))
# N, K = 7, 10
# A = [11, 12, 16, 22, 27, 28, 31]


def search(index):
    x = A[index]+K
    left = index
    right = N-1

    while (left < right):
        mid = (left+right)//2+1
        tmp_value = A[mid]

        if A[mid] <= x:
            left = mid
        else:
            right = mid-1
    return right


ans_count = 0
for i in range(N-1):
    tmp_index = search(i)
    ans_count += tmp_index-i
print(ans_count)
