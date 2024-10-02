import math
from itertools import permutations 

def prime_number(num):
    if num in [0,1]:
        return False
    
    count = 0
    for i in range(2, math.floor(num**0.5)+1):
        if num % i == 0:
            count += 1
    
    if count == 0:
        return True
    else:
        return False

def solution(numbers):
    numbers = list(numbers)
    
    answer = 0
    num_list = []
    for i in range(1,len(numbers)+1):
        perms = permutations(numbers, i)
        for p in perms:
            num = int(''.join(p))
            if num not in num_list:
                num_list.append(num)
                if prime_number(num) == True:
                    answer += 1
    
    return answer
