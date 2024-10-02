def solution(clothes):
    clothes_count = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in clothes_count.keys():
            clothes_count[clothes[i][1]] = 1
        else:
            clothes_count[clothes[i][1]] += 1
            
    answer = 1
    for i in clothes_count.values():
        answer *= (i+1)
    return answer -1




