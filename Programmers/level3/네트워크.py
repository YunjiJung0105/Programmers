# version 1 : 1D visited
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            BFS(i, visited, computers)
            answer += 1
    
    return answer


def BFS(start, visited, computers):
    queue = deque([(start)])
    visited[start] = True
    
    while queue:
        x = queue.popleft()
        
        for j in range(len(computers)):
            if computers[x][j] ==1 and visited[j] == False:
                queue.append(j)
                visited[j] = True
    
    
# version 2
from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque([])
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[i][j] == False:
                queue.append((i,j))
                visited[i][j] = True

                while queue:
                    x,y = queue.popleft()

                    for k in range(n):
                        if computers[x][k] == 1 and visited[x][k] == False:
                            queue.append((k,x))
                            visited[x][k] = True    # Why flipped???

                answer +=1
            
    return answer
        
