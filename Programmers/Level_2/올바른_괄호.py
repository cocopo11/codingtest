def solution(s):
    answer = []
    for i in s:
        if i == "(":
            answer.append(i)
        else:
            try:
                answer.pop()
            except IndexError:
                return False
    return len(answer) == 0