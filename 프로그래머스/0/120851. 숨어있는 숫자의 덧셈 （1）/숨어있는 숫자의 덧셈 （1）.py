def solution(my_string):
    
    result = 0

    for i in my_string :
        
        if i in ['1','2','3','4','5','6','7','8','9','0'] :
            i = int(i)
            result += i
        else :
            continue

    
    return result