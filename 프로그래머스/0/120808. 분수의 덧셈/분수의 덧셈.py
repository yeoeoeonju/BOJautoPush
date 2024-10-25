import math 
def solution(numer1, denom1, numer2, denom2):
    answer = []
    son = 0
    mom = 0
    
    
    if math.gcd(denom1, denom2) == 1 :
        son = denom1 * denom2
        mom = (numer1 * denom2) + (numer2 * denom1)
        
        
    else :
        if denom1 < denom2 :
            son = denom1 * math.gcd(denom1, denom2)
            mom = numer1 * math.gcd(denom1, denom2) + numer2
                
            
        elif denom1 > denom2:
            son = denom2 * math.gcd(denom1, denom2)
            mom = numer2 * math.gcd(denom1, denom2)
                
            
        else :
            son = denom1 
            mom = numer1 + numer2
    print(mom, son)
    while (True) :
        if math.gcd(mom, son) != 1 :
            gcd = math.gcd(mom, son)
            mom = mom // gcd
            son = son // gcd
        else :
            break
            
    return mom, son