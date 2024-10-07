def solution(before, after):
    
    before = list(before)
    after = list(after)
    
    for i in before :
        if i in after :
            index = after.index(i)
            after.pop(index)
    
    if len(after) > 0 :
        return 0
    else :
        return 1 
    
        
    
    
    