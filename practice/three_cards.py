N, K = map(int, input().split())
sum = 0

for i in range(1, N+1):
    max_tmp = min(-i+K-1, N)
    min_tmp = max(1, -i+K-N)
    if min_tmp <= max_tmp:
        sum += max_tmp-min_tmp+1

print(sum)
