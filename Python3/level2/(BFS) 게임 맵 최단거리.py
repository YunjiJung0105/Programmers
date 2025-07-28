from collections import deque

def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n,m = len(maps), len(maps[0])
    
    queue = deque()
    queue.append((0,0,1))
    visited = set()
    
    while queue:
        x,y,step = queue.popleft()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        
        if x==n-1 and y==m-1:
            return step
        
        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m and maps[x+dx[i]][y+dy[i]] == 1:
                queue.append((x+dx[i], y+dy[i], step+1))

    return -1
