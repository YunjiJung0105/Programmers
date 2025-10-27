from collections import Counter

def solution(s):
    s = s.replace('{', "")
    s = s.replace('}', "")
    s = s.replace(',', " ")
    s = s.split(' ')
    
    s_count = Counter(s)
    s_count = sorted(s_count, key=lambda x: -s_count[x])
    
    return list(map(int, s_count))
