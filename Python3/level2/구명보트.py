# 코드는 맞지만 런타임 문제...
def solution(people, limit):
    people.sort(reverse=True)
    
    answer = 0
    i = 0
    while people:
        a = people.pop(0)
        for j in range(len(people)-1,-1,-1):
            if people[j] <= limit-a:
                people.pop(j)
                break
        answer += 1
        i += 1
        
    return answer


# 시간 단축법
from collections import deque  # deque하면 시간 단축!

def solution(people, limit):
    people.sort()    # reverse하면 시간 초과!
    people = deque(people)
    
    answer = 0
    while people:
        if len(people)>1 and people[-1] + people[0] <= limit:
            people.popleft()
        answer += 1
        people.pop()
            
        
    return answer
