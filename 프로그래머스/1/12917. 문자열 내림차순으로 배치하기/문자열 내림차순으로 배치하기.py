def solution(s):
    
    
    s_lower = list(s)
    s_lower.sort(reverse=True)
    

    return ''.join(s_lower)