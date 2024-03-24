def solution(n):
    lst = list(str(int(n)))
    lst.sort(reverse = True)
    
    return int('' .join(lst))