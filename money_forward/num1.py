N = int(input())
A = list(map(int, input().split()))

seen = set()
ans = False

for i in range(N):
    if A[i] in seen:
        print(i + 1)
        ans = True
        break
    seen.add(A[i])

if not ans:
    print(-1)
