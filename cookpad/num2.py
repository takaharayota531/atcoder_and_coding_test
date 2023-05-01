import sys

args=sys.argv

K=int(args[1])
# K=3
# A=[4,2,1,9,10]
A=[]
try:
    while True:
      a=int(input())
      A.append(a)
except EOFError:
  pass
A.sort()
# print(A)
L=A[len(A)-1]

def check(A,K,key):
  divide_count=0
  prev=0
  
  for i in range(len(A)):
    if A[i]-prev>=key:
      divide_count+=1
      prev=A[i]

  if A[0]<=key:
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
