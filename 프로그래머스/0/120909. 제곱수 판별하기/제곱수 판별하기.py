import math

def solution(n):
    answer = 0
    
    answer = math.isqrt(n)
    
    if answer * answer == n :
        return 1
    else :
        return 2