def solution(my_string):
    answer_num = []
    answer_how = []
    
    my_string = my_string.split(' ')
    
    for i in my_string :
        if i.isdigit() == True :
            answer_num.append(int(i))
        else :
            answer_how.append(i)
            
    for i in range(len(answer_how)) :
        if answer_how[i] == '+':
            answer_num[i+1] = answer_num[i] + answer_num[i+1]
        else :
            answer_num[i+1] = answer_num[i] - answer_num[i+1]
            
    return answer_num[-1]

