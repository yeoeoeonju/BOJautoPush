def solution(n):
    
    if n == 1 :
        return 1
    
    else :
        lst = [0] * (n+1)
        
        lst[1] = 1
        lst[2] = 2
        
        for i in range(3, n+1) :
            lst[i] = (lst[i-2] + lst[i-1]) % 1234567
            
        return lst[-1]
    
    
    