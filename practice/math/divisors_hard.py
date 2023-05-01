N = int(input())
ans = N//3+N//5+N//7-N//(3*5)-N//(3*7)-N//(5*7)+N//(3*5*7)
print(ans)
