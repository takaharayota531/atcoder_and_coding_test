import numpy as np
H, W, N = map(int, input().split())
list = np.zeros((N, 4))
for i in range(N):
    a, b, c, d = map(int, input().split())
    list[i][0] = a
    list[i][1] = b
    list[i][2] = c
    list[i][3] = d

ans_array = np.zeros((H, W))

for i in range(N):
    a = int(list[i][0])
    b = int(list[i][1])
    c = int(list[i][2])
    d = int(list[i][3])

    ans_array[a-1:c, b-1:d] += 1
print("\n".join(" ".join(str(int(elem)) for elem in row) for row in ans_array))
