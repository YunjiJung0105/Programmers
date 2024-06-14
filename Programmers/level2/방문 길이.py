def solution(dirs):
    visited = []
    
    curr = [0,0]
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            nex = [curr[0], curr[1]+1]
        elif dirs[i] == 'D':
            nex = [curr[0], curr[1]-1]
        elif dirs[i] == 'R':
            nex = [curr[0]+1, curr[1]]
        else:
            nex = [curr[0]-1, curr[1]]
            
        if -5<=nex[0]<=5 and -5<=nex[1]<=5 and [curr,nex] not in visited and [nex,curr] not in visited:   # a->b 이든 b->a이든 똑같이 지나간 길이기 때문에 반대방향도 고려해야됨!!
            visited.append([curr,nex])
        if -5<=nex[0]<=5 and -5<=nex[1]<=5:
            curr = nex

    return len(visited)
