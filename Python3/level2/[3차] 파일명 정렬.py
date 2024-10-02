def solution(files):
    files_list = []
    for i in range(len(files)):
        f = list(files[i])
        HEAD = []
        NUMBER = []
        TAIL = []
        while f:
            if not f[0].isdecimal():
                HEAD.append(f[0])
                f.pop(0)
            else:
                break
        while f:
            if f[0].isdecimal() and len(NUMBER) <5:
                NUMBER.append(f[0])
                f.pop(0)
            else:
                break
        
        HEAD = ''.join(HEAD)
        NUMBER = ''.join(NUMBER)
        TAIL = ''.join(f)
                
        files_list.append([files[i], HEAD, NUMBER, TAIL])

    files_list.sort(key = lambda x: (x[1].lower(), int(x[2])))
  
    answer = []
    for i in range(len(files_list)):
        answer.append(files_list[i][0])
        
    return answer
