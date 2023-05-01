def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


N = int(input())
for i in range(1, N+1):
    tmp_ans = is_prime(i)
    if tmp_ans:
        print(i)
