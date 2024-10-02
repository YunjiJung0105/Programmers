def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
                
        answer.append(count)
            
    return answer


# 더 효율적으로!
def solution(prices):
    answer = list(range(len(prices)-1,-1,-1))
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            a = stack.pop()
            answer[a] = i-a
        stack.append(i)

    return answer
