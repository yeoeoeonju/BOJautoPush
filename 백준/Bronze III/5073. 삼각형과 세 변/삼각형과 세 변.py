while (True) :
    a, b, c = map(int, input().split())
    lst = [a, b, c]
    
    
    if a == b == c == 0 :
        break

    elif max(lst) >= (sum(lst) - max(lst)) :
        print('Invalid')
    elif a == b == c :
        print('Equilateral')
    elif a == b or a == c or b == c :
        print('Isosceles')
    else :
        print('Scalene')