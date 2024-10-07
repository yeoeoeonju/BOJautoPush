def solution(my_string):
    answer = []
    temp = ''
    for i in my_string :
        
        if i.isdigit() == True :
            temp += i
        else :
            if len(temp) >= 1 :
                
                answer.append(temp)
                temp = ''
    if len(temp) >= 1 :
        answer.append(temp)
        temp = ''
            
    
        
    return sum(int(i) for i in answer)


