def solution(n, times):
    left = min(times)
    right = max(times) * n
    
    while left <= right:
        people = 0
        mid = (left+right)//2
        
        for time in times:
            people += mid//time
            
            if people >= n:
                break
        
        if people >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer
