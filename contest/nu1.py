N,A,B=  map(int,input().split())
c=list(map(int,input().split()))
for i in range(N):
  if c[i]==A+B:
    
    print(i+1)
    break
  