def solution(n, words):
    
    temp = ''
    check_lst = []
    
    for i in range(len(words)-1):
        check_lst.append(words[i])
        
        if words[i][-1] == words[i+1][0] and words[i+1] not in check_lst and len(words[i]) != 1 :
            continue
        else:
            temp = words[i+1]
            return ([((i+1) % n) + 1 ,((i+1) //n)+1])
    
    if temp == '':
        return [0,0]

   