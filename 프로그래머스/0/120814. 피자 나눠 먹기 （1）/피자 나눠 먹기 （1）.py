def solution(n):
    answer = 0
    
    for i in range(n+1):
        
        if n <= 7 * i :
            answer = i
            break
            
    return answer