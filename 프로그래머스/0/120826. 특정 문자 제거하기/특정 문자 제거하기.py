def solution(my_string, letter):
    answer = []
    my_string = list(my_string)
    
    for i in range(len(my_string)) :
        if my_string[i] == letter :
            pass 
        else :
            answer.append(my_string[i])
    
        str = ''.join(answer)
        
    return str