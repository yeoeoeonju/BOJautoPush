def solution(num_list):
    num = len(num_list) -1
    answer = []
    
    for i in range(len(num_list)) :
        
        answer.append(num_list[num - i])
        
    return answer