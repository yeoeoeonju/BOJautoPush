def solution(numbers):
    answer = 0
    check = [1,2,3,4,5,6,7,8,9,0]
    
    for i in numbers:
        check.remove(i)
    
    return sum(check)