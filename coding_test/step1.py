from collections import deque
step=int(input())

def check(menu_info,T,D,N):
  if menu_info[D]["S"] >= N:
    for i in range(N):
      menu_info[D]["S"]-=1
      print("received order "+str(T)+" "+str(D))
  else:
    print("sold out "+str(T))    
  

if step==1:
  M=int(input())
  menu_info={}
  for i in range(M):
    D,S,P=list(map(int,input().split()))
    menu_info[D] = {
      "S": S,
      "P": P
    }
#   print(menu_info)
  
  try:
    while True:
      order,T,D,N=input().split()
      if order=="order":
        T=int(T)
        D=int(D)
        N=int(N)
        check(menu_info,T,D,N)
      else:
        break
  except EOFError:
    pass
elif step==2:
  M,K=map(int,input().split())
  order_info={}
  cooking = {}
  for i in range(M):
    D,S,P=list(map(int,input().split()))
    order_info[D] = {
      "S": S,
      "P": P
    }
    cooking[D] = 0
  waiting=deque()
  tmp_num=0
  try:
    while True:
      order=input()
      if order[0]=="r":
        re,buf,T,D=order.split()
        T=int(T)
        D=int(D)
        waiting.append([T,D])
        if tmp_num<K:
          waiting.popleft()
          cooking[D]+=1
          tmp_num += 1
          print(D)
          
        else:
          print('wait')
      
      elif order[0]=="c":
        c,D=order.split()
        D=int(D)
        if cooking[D]==0:
          print('unexpected input')
        else:
          cooking[D]-=1
          tmp_num-=1
          
          if len(waiting):
            next=waiting.popleft()
            print('ok '+str(next[1]))
            tmp_num += 1
            cooking[next[1]]+=1
          else:
            print('ok')
          
       
      else:
        break
  except EOFError:
    pass