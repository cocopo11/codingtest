from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for dungeon in permutations(dungeons):
        current_k = k
        count = 0 
        
        for i in dungeon:
            rq,cs = i
            if current_k >= rq:
                current_k -= cs
                count += 1
            else:
                break
        
        answer = max(answer, count)

    return answer