def frog_jump(h):
    s = [0]*(len(h)+1)
    s[1] = 0
    s[2] = h[0]

    for i in range(3, len(h)+1):
        s[i] = min(s[i-2]+abs(h[i]-h[i-2]), s[i-1]+abs(h[i]-h[i-1]))
