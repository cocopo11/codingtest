def solution(ingredient):
    answer = 0
    hb = []
    for i in ingredient:
        hb.append(i)
        if len(hb) < 4:
            continue
        if hb[-4:] == [1,2,3,1]:
            answer += 1
            for j in range(4):
                hb.pop()
    return answer