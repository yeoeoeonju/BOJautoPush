def solution(numbers):
    answer = []
    
    numbers.sort(reverse = True)
    
   
    answer.append(numbers[-1] * numbers[-2])
    answer.append(numbers[0] * numbers[1])
    return max(answer)
            
            