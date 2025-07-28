from collections import deque

def solution(tickets):
    answer = []
    
    queue = deque()
    queue.append(("ICN", ["ICN"], []))
    
    while queue:
        now, path, idxes = queue.popleft()
        
        if len(idxes) == len(tickets):
            answer.append(path)
            
        for idx, ticket in enumerate(tickets):
            if ticket[0] == now and idx not in idxes:
                queue.append((ticket[1], path+[ticket[1]], idxes+[idx]))
    
    
    answer.sort()
    return answer[0]
