from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x,0))
    visited = set()   # visited 필요!
    
    while queue:
        now, step = queue.popleft()
        
        if now > y or now in visited:
            continue     
        visited.add(now)
        
        if now == y:
            return step

        for k in [now*3, now*2, now+n]:   # 순서 주의!
            if k<=y and k not in visited:
                queue.append((k, step+1))
              
    return -1
