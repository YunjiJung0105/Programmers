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



# 더 쉽게!
import math
def solution(progresses, speeds):
    left = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
   
    answer = []
    for i in range(len(left)):
        if i == 0:
            answer.append(1)
            max_val = left[0]
        else:
            if left[i] > max_val:
                answer.append(1)
                max_val = left[i]
            else:
                answer[-1] += 1
                
    return answer
