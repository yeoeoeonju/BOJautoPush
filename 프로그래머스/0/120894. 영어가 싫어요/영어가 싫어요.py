def solution(numbers):
    answer = []
    start = 0
    number_names = {"one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9', "zero":'0'}
    
    while start < len(numbers) :
        found = False 
        
        for i in number_names :
            if numbers.find(i, start) == start:
                answer.append(number_names[i])
                start += len(i)
                found = True
                break
        if not found :
            break
    
    return int(''.join(answer))