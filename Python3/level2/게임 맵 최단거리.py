# version 1
from collections import deque
    
def BFS(maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n,m = len(maps), len(maps[0])
    
    queue = deque([(0,0,1)])
    visited = set()
    
    while queue:
        x,y, step = queue.popleft()
        
        if (x,y) in visited:
            continue
        visited.add((x,y))
        
        if x == n-1 and y == m-1:
            return step
            
        # next_x,next_y로 할게 아니라 그냥 x,y로 해야됨!!!
        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m and maps[x+dx[i]][y+dy[i]] != 0:
                next_x, next_y = x+dx[i], y+dy[i]
                queue.append((next_x,next_y,step+1))
                
                
    if (n-1,m-1) not in visited:
        return -1
        

def solution(maps):
    return BFS(maps)



#version 2
from collections import deque

def BFS(start_x, start_y, graph):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n = len(graph)
    m = len(graph[0])
    
    queue = deque([(start_x,start_y)])
    dist = [[987654321 for _ in range(m)] for _ in range(n)]
    dist[0][0] = 1    # Important!!!
    
    while queue:
        x,y = queue.popleft()
        count = dist[x][y]
        
        if x == (n-1) and y == (m-1):
            return dist[x][y]
        
        for i in range(4):
            next_x, next_y = x, y
            if 0 <= next_x+dx[i] < n and 0 <= next_y+dy[i] < m and graph[next_x+dx[i]][next_y+dy[i]] != 0:
                next_x += dx[i]
                next_y += dy[i]
                
            if dist[next_x][next_y] > count+1:
                dist[next_x][next_y] = count+1
                queue.append((next_x,next_y))
                
    return -1

def solution(maps):
    answer = BFS(0,0,maps)
    return answer
