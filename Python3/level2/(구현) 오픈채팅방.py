def solution(record):
    answers = []
    id_list = {}
    
    for r in record:
        if 'Enter' in r:
            id = r.split(' ')[1]
            name = r.split(' ')[2]
            id_list[id] = name
            answers.append(f'{id}님이 들어왔습니다.')
        elif 'Leave' in r:
            id = r.split(' ')[1]
            answers.append(f'{id}님이 나갔습니다.')
        else:
            id = r.split(' ')[1]
            name = r.split(' ')[2]
            id_list[id] = name

    
    new_answers = []
    for a in answers:
        id = a[:a.index('님')]
        name = id_list[id]
        a = name + a[a.index('님'):]
        new_answers.append(a)
        
    return new_answers
