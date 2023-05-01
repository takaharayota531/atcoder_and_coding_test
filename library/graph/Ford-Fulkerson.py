from typing import ChainMap


def ford_fulkerson(V,capacity,start,end):
  max_flow=0
  while True:
    visited=[False]*(V+1)
    flow=dfs_ff(start,end,10**9,visited,capacity)
    if not flow :
      break
    max_flow+=flow
    return max_flow
    
def dfs_ff(s,e,flow,visited,capacity):
  if (s==e):
    
    return flow 
  visited[s]=True 
  for i in range(V): 
    if capacity[s][i]>0  and not visited[i]:
      f=dfs_ff(i,e,min(flow,capacity[s][i]),visited,capacity)
      if f>=1:
        capacity[s][i]-=f 
        capacity[i][s]+=f 
        return f
  return 0
        
    



capacity =[
[0, 10, 10, 0, 0, 0], [0,0,0,4,8,0], [0,0,0,7,4,0], [0, 0, 0, 0, 0, 8], [0, 0, 0, 0, 0, 12], [0, 0, 0, 0, 0, 0]
]
max_flow=0
V=6
max_flow=ford_fulkerson(V,capacity,0,V-1)
print(max_flow)