def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]    
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    
    for i,v in enumerate(answers):
        if v == a1[i % len(a1)]:
            score[0] += 1
        if v == a2[i % len(a2)]:
            score[1] += 1
        if v == a3[i % len(a3)]:
            score[2] += 1
    
    answer = {1:score[0], 2:score[1], 3:score[2]}
    
    max_answer = max(answer.values())
    
    return [k for k,v in answer.items() if v == max_answer]