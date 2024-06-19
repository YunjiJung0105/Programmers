def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            a = stack.pop()
            answer[a] = numbers[i]
        stack.append(i)
                
    
    return answer
