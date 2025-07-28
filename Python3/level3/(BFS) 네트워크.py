from collections import deque

def solution(n, computers):
    answer = 0
    visited = set()
    
    for start_v in range(n):
        if start_v in visited:
            continue
        queue = deque([start_v])
        visited.add(start_v)
        
        while queue:
            now_v = queue.popleft()
            for next_v in range(n):
                if next_v == now_v:
                    continue
                if computers[now_v][next_v] == 1 and next_v not in visited:
                    queue.append(next_v)
                    visited.add(next_v)
                    
        answer += 1
    
    return answer
