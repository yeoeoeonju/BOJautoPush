def solution(num, k):
    answer = -1
    
    lst = []
    
    for i in str(num) :
        lst.append(i)
    
    for i in range(len(lst)) :
        if lst[i] == str(k):
            answer = i+1
            break
        else :
            continue
    return answer 