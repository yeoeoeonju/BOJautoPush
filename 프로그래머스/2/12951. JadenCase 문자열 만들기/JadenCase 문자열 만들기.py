def solution(s):
    
    lst = []
    
    for i in range(len(s)) :
        if s[i] == ' ':
            lst.append(i)
            
    a = list(s.split())
    
    for i in range(len(a)):
        a[i] = a[i].capitalize()
        
    aa = ''
    
    for i in a :
        aa += i
    
    aa = list(aa)
    
    for i in lst :
        aa.insert(i, ' ')
    ss = ''
    for i in aa :
        ss += i
        
    return ss

