def solution(s):
    answer = 0
    
    start = 0
    same = 0
    diff = 0
    for i in range(len(s)):
        if s[i] == s[start]:
            same += 1
        else:
            diff += 1
        if same == diff:
            start = i+1
            answer += 1
        if i == len(s)-1 and same != diff:
            answer += 1
    
         
    return answer
