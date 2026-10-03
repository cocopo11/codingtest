from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    nmbr = [i for i in numbers]
    temp = []
    
    for r in range(1,len(nmbr)+1):
        for i in permutations(nmbr,r):
            k = int(''.join(list(i)))
            if is_prime(k):
                if k not in temp:
                    temp.append(k)
            else:
                continue
    return len(temp)