def is_possible(n, diffs, times, limit):
    time = times[0]
    for i in range(1,len(diffs)):
        if n < diffs[i]:
            time += ((diffs[i]-n)*(times[i-1]+times[i])+times[i])
        else:
            time += times[i]
        if time > limit:
            return False
    return True

def solution(diffs, times, limit):
    answer = 0
    start = 1
    end = max(diffs) 
    
    while start <= end:
        mid = (start + end) // 2
        
        if is_possible(mid, diffs, times, limit):
            end = mid - 1
            answer = mid 
        else:
            start = mid + 1
    return answer