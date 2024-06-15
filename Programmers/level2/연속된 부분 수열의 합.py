# 투 포인터 이용해서 k보다 작으면 l을 크게, k보다 크면 r을 작게!
def solution(sequence, k):
    answers = []
    sum = sequence[0]
    l = 0
    r = 0
    
    while True:
        if sum < k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
        else:
            if sum == k:
              answers.append([l, r])
            sum -= sequence[l]
            if l >= len(sequence):
                break
            l += 1

    answers.sort(key=lambda x: (x[1]-x[0], x[0]))

    return answers[0]





