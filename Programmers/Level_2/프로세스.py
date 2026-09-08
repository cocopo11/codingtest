from collections import deque

def solution(priorities, location):
    temp = deque(enumerate(priorities))
    num = 0
    while len(temp) > 0:
        a,b = temp.popleft()
        for i,v in temp:
            if b < v:
                temp.append((a,b))
                break
        else:
            num += 1
            if a == location:
                return num