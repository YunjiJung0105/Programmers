# 무식한 방법...
from itertools import product
def solution(word):
    all = []
    for i in range(1,6):
        part = [''.join(j) for j in product(['A','E','I','O','U'], repeat=i)]
        all += part
    all.sort()
  
    return all.index(word)+1

  
# dfs로 풀어보기!
