def solution(box, n):
    answer = []
    
    for i in box :
        temp = 0
        temp = i // n 
        answer.append(temp)
    fl = 1
    for i in answer :
        fl *= i
    
    return fl