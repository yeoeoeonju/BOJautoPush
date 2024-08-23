def solution(t, p):
    a = ''
    n = len(p)
    lst = []
    answer = 0
    
    for i in range(len(t)-n+1) :


        for j in range(n) :
            a += t[i+j]

        lst.append(a)
        a = ''

    

    for i in lst :
        if int(i) <= int(p) :
            answer += 1
        else : 
            continue

    
    
    return answer