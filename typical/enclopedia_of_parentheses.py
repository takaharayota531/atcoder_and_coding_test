N = int(input())

if N % 2 == 0:

    # N = 2
    array = []
    for i in range(2**(N)):
        bit = format(i, f'0{N}b')
        array.append(bit)

    def check(array):
        ans_array = [True]*(2**N)
        for i in range(2**N):
            check_count = 0
            for j in range(N):
                tmp = array[i][j]
                if array[i][j] == '1':
                    check_count -= 1
                else:
                    check_count += 1

                if check_count < 0:
                    ans_array[i] = False
            if check_count != 0:
                ans_array[i] = False
        return ans_array

    ans = check(array)

    for i in range(2**N):
        if ans[i] == True:
            ans_print = array[i]

            print(ans_print.replace('1', ')').replace('0', '('))
