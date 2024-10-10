def solution(array):
    answer = 0
    array = ''.join(map(str, array))
    
    for i in array :
        if i == '7':
            answer += 1
            
    return answer