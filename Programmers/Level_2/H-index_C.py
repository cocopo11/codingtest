def solution(citations):
    c = sorted(citations)
    for i in range(len(c)):
        h = len(c) - i
        if c[i] >= h:
            return h
    return 0