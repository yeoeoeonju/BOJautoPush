def solution(n):
    answer = 0
    
    for i in range(1,n) :
        if i * (n//i) == n :
            answer += 1
            
    return answer+1
