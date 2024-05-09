def solution(phone_number):
    answer = []
    
    for i in range(len(phone_number)) :
        if i >= 4 :
            answer.append('*')
            continue
        
        answer.append(phone_number[len(phone_number) - i - 1])
    answer.reverse()
        
    return ''.join(answer)