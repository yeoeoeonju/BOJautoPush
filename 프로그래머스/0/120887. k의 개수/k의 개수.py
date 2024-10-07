def solution(i, j, k):
    answer = 0
    temp = []
    
    for a in range(i, j+1) :
        temp += list(str(a))
        
    for b in temp :
        if b == str(k) :
            answer += 1
    return answer