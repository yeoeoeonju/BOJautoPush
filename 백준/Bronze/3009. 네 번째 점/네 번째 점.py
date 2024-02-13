x_lst = []
y_lst = []

rest = []

for i in range(3) :
    x, y = map(int, input().split())

    x_lst.append(x)
    y_lst.append(y)

for i in range(len(x_lst)) :
    if x_lst.count(x_lst[i]) == 1 :
        rest.append(x_lst[i])
        
for i in range(len(x_lst)) :
    if y_lst.count(y_lst[i]) == 1 :
        rest.append(y_lst[i])

for i in rest :
    print(i, end = ' ')