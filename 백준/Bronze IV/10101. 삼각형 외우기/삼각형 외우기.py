lst = []
for i in range(3) :
    n = int(input())
    lst.append(n)

if sum(lst) == 180 :
    if lst[0] == lst[1] == lst[2] :
        print('Equilateral')
    elif (lst[0] == lst[1]) or (lst[1] == lst[2]) or (lst[0] == lst[2]) :
        print('Isosceles')
    else :
        print('Scalene') 
else : 
    print('Error')