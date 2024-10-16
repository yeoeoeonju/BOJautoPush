def solution(sides):
    answer = 0
    
    mx = max(sides)
    start = mx - min(sides)
    for i in range(start+1,mx+1) :
        answer += 1
    
    less = answer - 1
    
    return answer + less