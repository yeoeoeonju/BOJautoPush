def solution(common):
    answer = 0
    differ = []
    
    for i in range(len(common)-1) :
        differ.append(common[i+1] - common[i])
    
    print(differ)
    
    if len(set(differ)) == 1 :
        answer = common[-1] + differ[0] 
    else :
        answer = common[-1] + (differ[-1] // differ[-2]) * differ[-1]
    return answer