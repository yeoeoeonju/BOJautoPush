def solution(n):
    lst = []
    cnt = 0
    
    while n :
        lst.append(n % 3)
        n //= 3
        
    for i in range(len(lst)):
        cnt += lst[i] * (3**(len(lst)-i-1))
        
    return cnt