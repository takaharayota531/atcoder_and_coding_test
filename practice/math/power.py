# 繰り返し自乗法
def power(x, n):
    M = 10 ** 9+7
    if n == 0:
        return 1

    tmp = power(x*x % M, n//2)
    if n % 2 == 1:
        tmp = tmp*x % M

    return tmp


a, b = map(int, input().split())
value = power(a, b)
print(value)
