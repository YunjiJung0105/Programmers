# 합이 더 큰 queue에서 pop해서 다른 queue로 insert해주면 됨!
from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target = int((sum1 + sum2)/2)
    
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    for _ in range(len(queue1) * 4):  # queue1, queue2의 모든 원소를 pop, insert시켜도 답이 없으면 방법 없는 것!
        if sum1 > sum2:
            a = queue1.popleft()
            queue2.append(a)
            sum2 += a
            sum1 -= a
            answer += 1
        elif sum1 < sum2:
            a = queue2.popleft()
            queue1.append(a)
            sum1 += a
            sum2 -= a           
            answer += 1
        else:
            return answer
            
    return -1
