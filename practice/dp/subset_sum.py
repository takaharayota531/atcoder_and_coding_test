S, N = map(int, input().split())
A = list(map(int, input().split()))
# S, N = 3, 7
# A = [2, 2, 3]


check_list = [[False for _ in range(N+1)]
              for _ in range(S+1)]

check_list[0][0] = True

for i in range(1, S+1):
    for j in range(0, N+1):
        if check_list[i-1][j] == True:
            check_list[i][j] = True
        if A[i-1] <= j and check_list[i-1][j-A[i-1]]:
            check_list[i][j] = True

if check_list[S][N]:
    print('Yes')
else:
    print('No')
