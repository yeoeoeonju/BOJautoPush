def solution(n):
    answer = 1
    temp = 1
    
    while (True) :
        answer = answer * temp
    
        if answer > n :
            break
        
        temp += 1
          
    return temp-1
        
        