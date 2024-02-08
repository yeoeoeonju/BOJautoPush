while (True) :

    n = int(input())
    if n == -1 :
        break

    lst = []

    for i in range(1, n) :
        if n % i == 0 :
            lst.append(int(i))


    if sum(lst) == n :  

        print(n,'=', end=' ')

        for i in range(len(lst)) :

            if lst[i] == lst[-1] :
                print(lst[i])
            else:
                print(lst[i], '+ ', end = '')
    
    else:
        print(n, 'is NOT perfect.')