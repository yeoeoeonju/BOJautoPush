def solution(x, n):
    answer = []
    if x == 0 :
        for i in range(x, n):
            answer.append(i-i)
    else:
            
        for i in range(x,(x*n)+x,x) :
            answer.append(i)
    
    return answer