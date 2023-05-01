N=int(input())
array=[]
for i in range(N):
  tmp=list(map(int,input().split()))
  array.append(tmp)
# print(array)
# * thinking
# ! kk

ans="Yes"
for i in range(N):
  if i==0:
    check=(array[0][1]+array[0][2]-array[0][0])
    if check%2==1 or 0<check:
      ans="No"
      break
  else :
    check=abs(array[i][1]-array[i-1][1])+abs(array[i][2]-array[i-1][2])-(array[i][0]-array[i-1][0])
    if check%2==1 or 0<check:
      ans="No"
      break

print(ans)