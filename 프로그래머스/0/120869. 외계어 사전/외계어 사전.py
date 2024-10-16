def solution(spell, dic):
    answer = 0
    
    spell.sort()
    spell = ''.join(spell)
    check = []
    
    for i in dic :
        if len(spell) == len(i) :
            check.append(i)
        
    if not check :
        answer = 2
        
        
    for i in check :
        if ''.join(sorted(i)) == spell :
            answer = 1
            break
            
        else :
            answer = 2
        
    return answer
    