H,W=map(int,input().split())
h_list=[0]*H
w_list=[0]*W
h_list_b=[0]*H
w_list_b=[0]*W



for i in range(H):
  tmp_value=input()
  for j in range(W):
    if tmp_value[j]=="#":
      
      # print(tmp_value)
      h_list[i]+=1
      w_list[j]+=1
# print(h_list)      
for i in range(H):
  tmp_value=input()
  for j in range(W):
    if tmp_value[j]=="#":
      
      h_list_b[i]+=1
      w_list_b[j]+=1      

check_h=False
for i in range(H):
  count=0
  for j in range(H):
    if h_list[(j+i)%H]==h_list_b[(j)%H]:
      count+=1
    else:break
  if count==H:
    check_h=True
    break 
check_w=False
for i in range(W):
  count=0
  for j in range(W):
    if w_list[(j+i)%W]==w_list_b[(j)%W]:
      count+=1
  if count==W:
    check_w=True
    break
if check_w and check_h :
  print("Yes")
else:
  print("No")