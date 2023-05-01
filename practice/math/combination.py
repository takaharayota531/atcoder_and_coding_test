# 繰り返し自乗法
def power(x, n):
    M = 10 ** 9+7
    if n == 0:
        return 1

    tmp = power(x*x % M, n//2)
    if n % 2 == 1:
        tmp = tmp*x % M

    return tmp


def factorial_list(n):
    M = 10 ** 9+7
    l = [1]*(n+1)
    i = 2
    while (i <= n):
        l[i] = l[i-1]*i % M
        i += 1
    return l[n]


def combination(n, r):
    M = 10 ** 9+7
    ans = factorial_list(n)*power(factorial_list(n-r), M -
                                  2) % M*power(factorial_list(r), M-2) % M
    return ans


n, r = map(int, input().split())

ans = combination(n, r)
print(ans)
