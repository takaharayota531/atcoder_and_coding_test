import heapq
def dijkstra(V,edges):
  inf=float('inf')
  done=[False]*V
  dist=[inf]*V
  dist[0]=0
  node_heap=[]
  heapq.heappush(node_heap,[dist[0],0])
  
  while node_heap:
    
    tmp =heapq.heappop(node_heap)
    cur_node=tmp[1]
    if (not done[cur_node]): 
      for e in edges[cur_node]:
        if dist[e[0]]>dist[cur_node]+e[1]:
          dist[e[0]]=dist[cur_node]+e[1]
          heapq.heappush(node_heap,[dist[e[0]],e[0]])
      
    done[cur_node]=True
  
  for i in range(V):
    if not done[i]:
      dist[i]=-1
  return dist

N,M=map(int,input().split())
edges_list=[[] for _ in range(N)]
for i in range(M):
  a,b,c=list(map(int,input().split()))
  edges_list[a-1].append([b-1,c])
  edges_list[b-1].append([a-1,c])

dist=dijkstra(N,edges_list)
for i in range(N):
  print(dist[i])