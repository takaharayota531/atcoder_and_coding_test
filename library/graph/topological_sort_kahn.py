from collections import deque

def KahnTopo(V,E, edges):
  indeg=[0]*V
  outedge=[[] for _ in range(V)]
  
  for v_from , v_to in edges:
    indeg[v_to]+=1
    outedge[v_from].append(v_to)
    
  sorted_g=list(v for v in range(V) if indeg[v]==0)
  deq=deque(sorted_g)
  
  while deq:
    
    v=deq.popleft()
    for u in outedge[v]:
      indeg[u]-=1
      E-=1
      
      
      if indeg[u]==0:
        deq.append( u)
        sorted_g.append(u)
  
  if E!=0:
    return -1
  
  return sorted_g



V = 5 # ノードの総数
E = 6 # 辺の総数
# 有向辺の配列
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 4]]
ans=KahnTopo(V,E,edges)

print (ans)