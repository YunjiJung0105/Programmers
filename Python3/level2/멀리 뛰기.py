# 피보나치 수열!
def solution(n):
    if n <= 2:
        return n
    a = 1
    b = 2
    c = a+b
    for i in range(n-3):
        a,b = b, c
        c = a+b
    
    return c%1234567
