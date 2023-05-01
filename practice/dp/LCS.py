S = input()
T = input()


def LCS(S, T):
    s_len = len(S)
    t_len = len(T)

    dp = [[0 for _ in range(t_len+1)]for _ in range(s_len+1)]

    for i in range(1, s_len+1):
        for j in range(1, t_len+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[s_len][t_len])


LCS(S, T)
