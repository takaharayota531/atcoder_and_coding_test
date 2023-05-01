import heapq

def prim(V,e_list):
  edges_from=[[]for _ in range(V)]
  
  for e in e_list:
    edges_from[e[0]].append([e[2],e[0],e[1]])
  
  e_heapq=[]
  mst=[]
  
  included=[False]*V
  start=0
  included[start]=True
  for e in edges_from[start]:
    heapq.heappush(e_heapq,e)
  
  while(len(e_heapq)):
    min_edge=heapq.heappop(e_heapq)
    
    if not included[min_edge[2]]:
      included[min_edge[2]]=True
      mst.append([min_edge[0],min_edge[1],min_edge[2]])
      for e in edges_from[min_edge[2]]:
        if not included[e[2]]:
          heapq.heappush(e_heapq,e)
  
  mst.sort()
  # print(mst)
  sum=0
  for i in range(len(mst)):
    sum+=mst[i][0]
    # print(mst[i][0])
  print(sum)
  
N,M=map(int,input().split())
edges_list=[]
for i in range(M):
  a,b,c=list(map(int,input().split()))
  edges_list.append([a-1,b-1,c])
  edges_list.append([b-1,a-1,c])
prim(N,edges_list)

# edges_list = [[0, 1, 5], [0, 2, 4], [1, 0, 5], [1, 3, 3], [1, 5, 9], [2, 0, 4], [2, 3, 2], [2, 4, 3], [3, 1, 3], [3, 2, 2], [3, 6, 7],
# [3, 7, 5], [4, 2, 3], [4, 6, 8], [5, 1, 9], [6, 3, 7], [6, 4, 8],
# [6, 7, 1], [7, 3, 5], [7, 6, 1]]
# prim(8,edges_list)
