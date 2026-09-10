def solution(clothes):
    count = {}
    answer = 1
    
    for name,kind in clothes:
        count[kind] = count.get(kind,0) + 1
    
    for i in count.values():
        answer *= i+1
        
    return answer - 1