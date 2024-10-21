import math

def solution(a, b):
    if a == b :
        return 1
    c = b // math.gcd(a, b)
    
    while (True) :
        if c%2 : break
        c = c // 2
    while (True) :
        if c%5 : break
        c = c // 5
    
    return 1 if c==1 else 2
