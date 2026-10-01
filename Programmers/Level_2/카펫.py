def solution(brown, yellow):
    n = int(yellow**0.5)
    for i in range(1,n+1):
        if yellow % i == 0:
            w = yellow // i
            if 2*(w+i) + 4 == brown:
                return (w+2,i+2)