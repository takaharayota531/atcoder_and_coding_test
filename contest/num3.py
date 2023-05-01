H,W=map(int,input().split())
c=[[0 for _ in range(W)]for _ in range(H)]
ans=[0]*min(H,W)

for i in range(H): 
  tmp_value=input()
  for j in range(W):
    if tmp_value[j]=="#":
      c[i][j]=1
      
def check(i,j):
  if c[i-1][j]==0 and c[i+1][j]==0 and c[i][j-1]==0 and c[i][j+1]==0:
    
    return True
  else:
    return False
 
def search(i,j):
  n=1
  check=False
  while True: 
    
    if 0<=i-n and  0<=j-n and  i+n<= H-1 and j+n<= W-1:
      if c[i-n][j-n]==1 and c[i+n][j-n]==1 and c[i-n][j+n]==1 and c[i+n][j+n]==1:
        check=True
        n+=1
        
      else:
        break
    else:
      break
  return n-1,check
for i in range(H):
  for j in range(W):
    if 0<=i-1 and 0<=j-1 and i+1<=H-1 and j+1<=W-1 and c[i][j]==1: 
      tp=check(i,j)
      if tp:
        count,checkw=search(i,j)
        if checkw:
          ans[count-1]+=1
print(*ans)
# print(ans.replace("]","").replace("[","").replace(",",""))