N, W = map(int, input().split())
value_list = []
for i in range(N):
    w, v = map(int, input().split())
    value_list.append([w, v])

dp = [[0 for _ in range(W+1)]for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        if 0 <= j-value_list[i-1][0]:
            dp[i][j] = max(dp[i-1][j-value_list[i-1][0]] +
                           value_list[i-1][1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][W])
