N,L=map(int,input().split())
K=int(input())
A=list(map(int,input().split()))
# N=3
# L=34
# K=1
# A=[8,13,26]

def check(A,K,key):
  divide_count=0
  prev=0
  
  for i in range(len(A)):
    if A[i]-prev>=key:
      divide_count+=1
      prev=A[i]

  if L-prev>=key:
    divide_count+=1
  if divide_count>=K+1:
    return True 
  else:
    return False
  

left=0
right=L
ans=0
while(left<=right):
  key=(right+left)//2
  if check(A,K,key)==True:
    left=key+1 
    ans=key
  else:
    right=key-1

print(ans)
