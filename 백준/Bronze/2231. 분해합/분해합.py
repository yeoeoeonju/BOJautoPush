n = int(input())

cons_list = list()

for j in range(0, n) :
    sum_as = 0
    
    for i in str(j) :
        sum_as += int(i)

    if sum_as + j == n :
        cons_list.append(j)

if len(cons_list) == 0:
    print(0)
else :
    print(min(cons_list))