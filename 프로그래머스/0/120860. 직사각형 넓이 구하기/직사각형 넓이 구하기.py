def solution(dots):
    left = []
    right = []
    
    for i in dots :
        left.append(i[0])
        right.append(i[1])
        
    print(left, right)
    
    return (max(left) - min(left)) * (max(right) - min(right))
    