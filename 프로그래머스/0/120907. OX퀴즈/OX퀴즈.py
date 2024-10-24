def solution(quiz):
    answer = []
    
    for i in quiz :
        left, right = i.split('=')
        left = left.split()
        print(left)
        print(right)
        
        if left[1] == '+' :
            test = int(left[0]) + int(left[-1])
        elif left[1] == '-' :
            test = int(left[0]) - int(left[-1])
            
        if test == int(right) :
            answer.append("O")
        else :
            answer.append("X")
    return answer