N, Q = map(int, input().split())
A = list(map(int, input().split()))
list = []
for i in range(Q):
    L, R = (map(int, input().split()))
    list.append([L, R])
# print(list)
sum_list = []
sum_list.append(0)
sum = 0
for i in range(N):
    sum += A[i]
    sum_list.append(sum)
for i in range(Q):
    L = list[i][0]
    R = list[i][1]
    tmp_ans = sum_list[R]-sum_list[L-1]
    print(tmp_ans)
