def solution(array, height):
    
    n = 0
    
    for i in range(len(array)):
        if height < array[i] :
            n += 1
    
    return n