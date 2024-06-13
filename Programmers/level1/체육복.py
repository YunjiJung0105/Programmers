def solution(n, lost, reserve): 
    set_lost = list(set(lost) - set(reserve))
    set_reserve = list(set(reserve) - set(lost))
    
    answer = n - len(set_lost)
    
    for i in range(len(set_lost)):
        j = 0
        while set_reserve and j < len(set_reserve):
            if abs(set_lost[i]-set_reserve[j]) == 1:
                answer += 1
                set_reserve.pop(j)
                break
            j += 1
    
    return answer
    
