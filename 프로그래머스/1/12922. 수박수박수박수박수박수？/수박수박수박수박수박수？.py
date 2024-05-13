def solution(n):
    answer = []
    lst = ['수', '박']
    for i in range(n) :
        
        if i >= len(lst) :
            answer.append(lst[i%2])
        else :
            answer.append(lst[i])
            
        
    return ''.join(answer)