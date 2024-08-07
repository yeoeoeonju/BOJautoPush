def solution(hp):
    
    ant = 0

    while (True) :
        ant += hp // 5 
        hp = hp % 5

        ant += hp // 3
        hp = hp % 3

        ant += hp // 1
        hp = hp % 1

        if hp == 0 :
            break
        
    return ant