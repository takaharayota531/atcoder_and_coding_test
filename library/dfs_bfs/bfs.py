from collections import deque


def bfs(edges, start, end):
    waiting = deque()
    V = len(edges)

    done = [0]*V
    done[start] = 2
    
    for n in edges[start]:
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
                    waiting.append(n)
            

edges_list = [
    [1, 2],
    [0, 3, 5],
    [0, 3, 4],
    [1, 2, 5],
    [2, 6],
    [1, 3, 7],
    [4],
    [5]
]

bfs(edges_list,2,5)
