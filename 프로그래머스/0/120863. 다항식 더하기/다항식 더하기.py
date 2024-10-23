def solution(polynomial):
    answer = [i.strip() for i in polynomial.split('+')]
    
    poly_num = []
    only_num = []
    
    for i in answer :
        
        if "x" in i :
            if len(i) == 1 :
                poly_num.append(1)
            
            else :
                temp = ''
                for num in i :
                    if num.isdigit() == True :
                        temp += num
                    else :
                        poly_num.append(int(temp))
        else :
            only_num.append(int(i))
    
    
    print(poly_num)
    print(only_num)
    
    if sum(poly_num) == 0 :
        
        if sum(only_num) == 0 :
            return 0
        else :
            return str(sum(only_num))
    else :
        if sum(poly_num) == 1 and sum(only_num) > 0 :
            return 'x' + ' + ' + str(sum(only_num))
        elif sum(poly_num) > 1 and sum(only_num) > 0 :
            return str(sum(poly_num)) + "x + " + str(sum(only_num))
        elif sum(poly_num) == 1 and sum(only_num) == 0 :
            return 'x'
        else :
            return str(sum(poly_num)) + 'x'
    
    
    