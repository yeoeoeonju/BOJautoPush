def solution(my_str, n):
    answer = []
    
    
    while my_str:
        temp = my_str[:n]
        answer.append(''.join(temp))
        my_str = my_str[n:]
    
    return answer