def solution(s):
    answer = []
    fin = ''
    s = list(s)
    print(s)
    
    for i in s :
        my_list = [x for x in s if x != i] 
        answer.append([abs(len(my_list) - len(s)), i])
    
    answer.sort()
    
    for i in range(len(answer)) :
        if answer[i][0] == 1 :
            fin += answer[i][1]
   
    return fin