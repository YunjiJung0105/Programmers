def solution(progresses, speeds):
    answer = []
    
    days = [(100-p)//s if (100-p)%s==0 else (100-p)//s+1 for p,s in zip(progresses,speeds)]
    
    i = 0
    max_day = days[0]
    while i < len(days):
        if i == 0:
            count = 1
        else:
            if days[i] <= max_day:
                count += 1
            else:
                answer.append(count)
                count = 1
                max_day = days[i]
        i += 1
        
    if sum(answer) != len(progresses):
        answer.append(count)
    return answer
