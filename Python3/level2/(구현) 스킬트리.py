def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        left = ''
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                left += skill_tree[i]
                
        if left == skill[:len(left)]:
            answer += 1
        
    return answer
