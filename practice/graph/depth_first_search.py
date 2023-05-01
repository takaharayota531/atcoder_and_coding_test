
from collections import deque


def bfs(edges,start):
  V=len(edges)
  done=[0]*V
  done[start]=2
  waiting=deque()
  
  for n in edges[start]:
    done[n]=1
    waiting.append(n)
  
  while(len(waiting)):
    cur_node=waiting.popleft()
    if done[cur_node]!=2:
      done[cur_node]=2
    for n in edges[cur_node]:
      if done[n]==0:
        done[n]=1
        waiting.append(n)  

  return done

N,M=map(int,input().split())
edges_list=[[]for _ in range(N)]

for i in range(M):
  A,B=map(int,input().split())
  edges_list[A-1].append(B-1)
  edges_list[B-1].append(A-1)

done_list=bfs(edges_list,0)
ans=True
for i in range(N):
  if done_list[i]==0:
    ans=False
    break

if ans==True:
  print('The graph is connected.')
else:
  print('The graph is not connected')