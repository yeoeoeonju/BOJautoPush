def solution(arr):
    
    tmp = min(arr)

    if len(arr) == 1 :
        result = [-1]
        return result

    else :

        arr.remove(tmp)
    
        return arr