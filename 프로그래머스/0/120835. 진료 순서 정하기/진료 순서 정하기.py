def solution(emergency):
    answer = []
    temp = emergency.copy()
    temp.sort(reverse = True)
    
    for i in emergency :
        answer.append(temp.index(i)+1)
        
    return answer