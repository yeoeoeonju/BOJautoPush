import math

def solution(a, b):
    
    if a == b :
        return 1
    
    gcd = math.gcd(a, b)
    
    c = b // gcd 
    
    while (True) :
        if c % 2 :
            break
        else :
            c = c // 2
    
    while (True) :
        if c % 5 :
            break
        else :
            c = c // 5
            
    return 1 if c == 1 else 2
    