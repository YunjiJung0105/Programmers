from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x,0))
    visited = set()
    
    while queue:
        now, step = queue.popleft()
        
        if now == y:
            return step
        
        if now > y or now in visited:   # 필요!!
            continue
        visited.add(now)
        
        for i in [now*3, now*2, now+n]:
            if i <= y and i not in visited:  # 여기서 같은 숫자가 여러번 append될 수 있음
                queue.append((i,step+1))
            
    return -1
