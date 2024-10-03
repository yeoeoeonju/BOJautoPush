def solution(num_list, n):
    answer = []
    temp = []
    for i in range(len(num_list)) :
        temp.append(num_list[i])
        
        if len(temp) % n == 0 :
            answer.append(temp)
            temp = []
        
    return answer