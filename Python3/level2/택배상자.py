def solution(order):
    answer = 0
    j = 0
    stack = []
    
    for i in range(1,len(order)+1):
        stack.append(i)
        while stack and stack[-1] == order[j]:
            stack.pop(-1)
            j += 1
            answer += 1

    return answer
