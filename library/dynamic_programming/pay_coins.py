def pay_coins():
    coins = [1, 8, 13]
    amount = 100
    dp = [0 for i in range(amount+1)]

    for i in range(1, amount+1):
        tmp_min = 10**6

        for j in range(len(coins)):
            if (0 <= i-coins[j]) and (tmp_min > dp[i-coins[j]]):
                tmp_min = dp[i-coins[j]]
            dp[i] = tmp_min+1
