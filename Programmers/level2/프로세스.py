def solution(priorities, location):
    idx = [i for i in range(len(priorities))]
    stack = []
    
    while priorities:
        if priorities[0] == max(priorities):
            stack.append(idx[0])
            priorities.pop(0)
            idx.pop(0)
        else:
            priorities.append(priorities[0])
            idx.append(idx[0])
            priorities.pop(0)
            idx.pop(0)
            
            
    return stack.index(location) + 1
    
