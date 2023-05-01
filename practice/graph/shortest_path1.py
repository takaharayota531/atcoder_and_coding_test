from collections import deque


def bfs(edges, start):
    waiting = deque()
    V = len(edges)
    distance_list=[-1]*V
    distance_list[start]=0
    done = [0]*V
    done[start] = 2
    
    for n in edges[start]:
        distance_list[n]=distance_list[start]+1
        done[n]=1
        waiting.append(n)
    
    while(len(waiting)):
        cur_node=waiting.popleft()
        if done[cur_node]!=2:
            done[cur_node]=2
            # print('Moved to {}'.format(cur_node))
            # if(end == cur_node):
            #     print('=FOUND!=')
            for n in edges[cur_node]:
                if done[n]==0:
                    done[n]=1
                    distance_list[n]=distance_list[cur_node]+1
                    waiting.append(n)
    
    return distance_list      


N,M=map(int,input().split())


edges_list=[[]for _ in range(N)]

for i in range(M):
  A,B=map(int,input().split())
  edges_list[A-1].append(B-1)
  edges_list[B-1].append(A-1)

distance_list=bfs(edges_list,0)
for i in range(N):
  print(distance_list[i])