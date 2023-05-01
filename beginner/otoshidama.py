N,Y=map(int,input().split())
Y=Y/1000

z=0
flag=False
while(z<=N):
  x=(Y-z)/5-(N-z)
  y=2*(N-z)-(Y-z)/5
  if (Y-z)%5==0 and 0<=x and 0<=y:
    flag=True
    break
  else:
    z+=1

if flag==True:
  print(int(x),int(y),int(z))
else:
  print(-1,-1,-1)

# a=b=0
# x=10000
# y=5000
# z=1000

# tmp_ams=0
# while (a<N):

#   tmp_ans=x*(N-b)+y*(b-a)+z*a
#   if tmp_ans<Y and b<N:
#     b+=1
#   elif Y<tmp_ans and a<b and b<=N:
#     a+=1
#   elif tmp_ans==Y:
#     # print(a,b-a,N-b)
#     break

# tmp_ans=x*(N-b)+y*(b-a)+z*a
# if tmp_ans
#   print(a,b-a,N-b)
# else:
#   print(-1,-1,-1)