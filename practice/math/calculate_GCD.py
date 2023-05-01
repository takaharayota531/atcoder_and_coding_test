def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = ext_gcd(b, a % b)
        return d, y, x-(a//b)*y


A, B = map(int, input().split())

a, b, c = ext_gcd(A, B)
print(a)
