def max_sum(a):
    s = [0]*(len(a)+1)

    for i in range(1, len(a)+1):
        s[i] = max(s[i-1], s[i-1]+a[i-1])

    return s
