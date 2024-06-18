# def solution(s):
#     stack = []
    
#     for i in s:
#         if i == '(':
#             stack.append(i)
#         else:
#             if stack == []:
#                 return False
#             else:
#                 stack.pop()
                
#     return stack == []


def solution(s):
    stack = []

    for i in range(len(s)):
        if stack:
            if stack[-1]+s[i] == '()':
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if stack:
        return False
    return True
