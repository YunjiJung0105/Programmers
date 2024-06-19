# 시간 단축 위해 몫, 나머지 이용!
def solution(n, left, right):
    array = []
    a,b = left//n, left%n
    c,d = right//n, right%n
    
    for i in range(a, c+1):
        array = array + [i+1]*(i+1)
        array = array + list(range(i+2,n+1))

    return array[b:(d-n+1)] if d-n+1 < 0 else array[b:]

    
    
    
    
    
    
        
    
