

def dijkstra(V,e_list):
  inf=float('inf')
  
  done=[False]*V
  dist=[inf]*V
  dist[0]=0
  
  while (1):
    cur_node=-1
    tmp_min_dist=inf
    
    for i in range(V):
      if (not done[i]) and(tmp_min_dist>dist[i]):
        tmp_min_dist=dist[i]
        cur_node=i
    if cur_node==-1:
      break
    for e in e_list[cur_node]:
      if dist[e[0]]>dist[cur_node]+e[1]:
        dist[e[0]]=dist[cur_node]+e[1]
      
    done[cur_node]=True
  
  print(dist)






edges_list = [[[1, 5], [2, 4]], [[0, 5], [3, 3], [5, 9]],
[[0, 4], [3, 2], [4, 3]],
[[1, 3], [2, 2], [5, 1], [6, 7]], [[2, 3], [6, 8]],
[[1, 9], [3, 1], [6, 2], [7, 5]], [[3, 7], [4, 8], [5, 2], [7, 2]], [[5, 5], [6, 2]]]
dijkstra(8,edges_list)