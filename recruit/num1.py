n=int(input())

for i in range(n):
  a,b=map(int,input().split())
  
  if b<=60 and a+b<=100:
    print('fail')
  elif b<=60 or a+b<=100:
    print('reexamination')
  else:
    print('pass')
    
    
    