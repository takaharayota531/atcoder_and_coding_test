def knapsack(W, N, weight, value):
    dp = [[-1 for _ in range(W+1)]
          for _ in range(N+1)]

    for j in range(W+1):
        dp[0][j] = 0

    for i in range(1, N+1):
        for j in range(W+1):
            if j > weight[i-1]:
                dp[i][j] = max(dp[i-1][j-weight[i-1]]+value[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[N][W]


W = 15
N = 6
weight = [11, 2, 3, 4, 1, 5]
value = [15, 3, 1, 4, 2, 8]
ans = knapsack(W, N, weight, value)
