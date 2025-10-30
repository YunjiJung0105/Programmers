# 시간 초과 유의!
from collections import Counter

def solution(weights):
    weights_count = Counter(weights)
    answer = 0
    
    # 1:1
    for w in weights_count:
        answer += weights_count[w] * (weights_count[w]-1) // 2
        
    # 1:2, 2:3, 3:4
    for w in weights_count:
        if w/2 in weights_count:
            answer += weights_count[w] * weights_count[w/2]
        if w*2/3 in weights_count:
            answer += weights_count[w] * weights_count[w*2/3]
        if w*3/4 in weights_count:
            answer += weights_count[w] * weights_count[w*3/4]
    
    return answer
