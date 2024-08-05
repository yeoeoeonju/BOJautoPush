def solution(my_string, n):
    
    temp = my_string
    answer = ''
    for i in temp :
        answer += i * n
        
    return answer