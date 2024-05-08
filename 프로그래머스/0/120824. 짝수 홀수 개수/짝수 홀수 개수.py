def solution(num_list):
    answer = []
    hol = 0
    zzak = 0
    
    for i in num_list :
        if i % 2 == 0 :
            hol += 1
        else :
            zzak += 1
    
    answer.append(hol)
    answer.append(zzak)
    return answer