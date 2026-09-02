def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    return sorted(answer) or [-1]