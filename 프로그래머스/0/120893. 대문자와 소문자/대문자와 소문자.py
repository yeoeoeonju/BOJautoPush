def solution(my_string):
    
    new_string=''
    
    for i in range(len(my_string)) :

        if my_string[i] in 'abcdefghijklmnopqrstuvwxyz' :
            new_string += my_string[i].upper()
        else :
            new_string += my_string[i].lower()
    
    return new_string