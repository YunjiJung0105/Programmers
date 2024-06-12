from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(numbers[0],0), (-numbers[0],0)])
    
    while queue:
        x, idx = queue.popleft()
        idx += 1
        
        if idx < len(numbers):
            queue.append((x+numbers[idx], idx))
            queue.append((x-numbers[idx], idx))
            
        else:
            if x == target:
                answer += 1
    
    return answer
