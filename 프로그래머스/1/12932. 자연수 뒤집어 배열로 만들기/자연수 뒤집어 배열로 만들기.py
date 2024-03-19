def solution(n):
    n = str(n)
    answer = []
    for i in range(len(n)) :
        a = n[len(n)-1-i]
        a = int(a)
        answer.append(a)
    
    
    return answer