def solution(elements):
    double_elements = elements * 2
    all = [sum(elements)]
    
    for i in range(1, len(elements)):
        for j in range(len(elements)):
            all.append(sum(double_elements[j:(j+i)]))
        
    all = set(all)
    return len(all)
