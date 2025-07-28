import string

def solution(msg):
    dictionary = list(string.ascii_uppercase)
    answer = []
    

    while msg:
        start = 0
        end = 1
        while end <= len(msg) and msg[start:end] in dictionary:   # end <= len(msg) 안 해주면 런타임 에러!
            end += 1
        answer.append(dictionary.index(msg[start:(end-1)])+1)
        dictionary.append(msg[start:end])
        msg = msg[(end-1):]
        
    return answer
