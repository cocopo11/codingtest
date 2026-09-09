def solution(participant, completion):
    count_1 = {}
    count_2 = {}
    
    for i in participant:
        count_1[i] = count_1.get(i,0) + 1
        
    for j in completion:
        count_2[j] = count_2.get(j,0) + 1
    
    for k in count_1:
        if count_1[k] != count_2.get(k, 0):
            return k