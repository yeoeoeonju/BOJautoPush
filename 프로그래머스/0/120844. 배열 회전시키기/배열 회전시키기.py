def solution(numbers, direction):
    answer = [0] * len(numbers)
    
    if direction == 'right' :
        
        answer[0] = numbers[-1]
        answer[-1] = numbers[-2]
        
        for i in range(1, len(numbers)-1):
            answer[i] = numbers[i-1]
        
        return answer
    else :
        answer[0] = numbers[1]
        answer[-1] = numbers[0]
        for i in range(1, len(numbers)-1) :
            answer[i] = numbers[i+1]
        return answer
        
        