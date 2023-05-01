inf =float('inf')
def warshall_floyd(V,e_matrix):
  dist=e_matrix
  for i in range(V):
    for j in range(V):
      for k in range(V):
        if dist[i][k]!=inf and dist[k][j]!=inf:
          dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
  print(dist)
  



edges_matrix=[
  [],
  [],
  
]