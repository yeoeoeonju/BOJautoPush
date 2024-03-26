def solution(x):
    
    lst = list(str(x))
    a = 0
    
    for i in lst :
        a += int(i)
    
    if x % a == 0:
        return True
    else :
        return False