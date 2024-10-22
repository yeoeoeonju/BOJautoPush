def solution(A, B):
    answer = 0
    
    count = 0
    
    for i in range(1, len(A)) :
        slide = A[:len(A)-i]
        slide_left = A[len(A)-i:]
        count += 1
        
        if slide_left + slide == B :
            answer = 1
            
            break
        else :
            answer = -1
            continue
    
        
    if answer == 1 :
        return count
    else :
        if answer == -1 :
            if A == B :
                return 0
            else :
                return -1
        else :
            return 0