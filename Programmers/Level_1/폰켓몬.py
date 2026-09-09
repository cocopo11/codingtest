def solution(nums):
    s = set(nums)
    return min(len(s),len(nums)//2)