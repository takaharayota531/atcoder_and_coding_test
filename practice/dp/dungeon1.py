N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


ans_list = [0]*(N+1)
ans_list[2] = A[0]

for i in range(3, N+1):
    ans_list[i] = min(ans_list[i-1]+A[i-2],
                      ans_list[i-2]+B[i-3])
print(ans_list[N])
