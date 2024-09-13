def solution(numbers):
    answer = []
    
    numbers.sort(reverse = True)
    
    if numbers[-1] < 0 and numbers[-2] < 0 :
                answer.append(numbers[-1] * numbers[-2])
                answer.append(numbers[0] * numbers[1])
                return max(answer)
            
        
    else :
        return numbers[0] * numbers[1]
            