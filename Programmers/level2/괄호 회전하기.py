def determine(string):
    right = ['()','[]','{}']
    stack = []
    
    for i in range(len(string)):
        if stack:
            if stack[-1] + string[i] in right:
                stack.pop()
            else:
                stack.append(string[i])
            
        else:
            stack.append(string[i])
            
    if stack:
        return 0
    else: 
        return 1
    

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        string = list(s[i:] + s[:i])
        answer += determine(string)
        
    return answer
