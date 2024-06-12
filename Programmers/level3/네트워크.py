from collections import deque

def BFS(start, visited, graph):
    queue = deque([(start)])
    visited[start] = True
    
    while queue:
        x = queue.popleft()
        
        for i in range(len(graph)):
            if x != i and graph[x][i] == 1:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            BFS(i, visited, computers)
            answer += 1
    return answer
