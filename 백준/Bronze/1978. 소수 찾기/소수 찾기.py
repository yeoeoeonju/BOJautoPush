N = int(input())

arr = list(map(int, input().split()))

summ = 0

for i in arr :
    lst = []
    for j in range(1, i+1) :
        if i % j == 0 :
            lst.append(j)

            if lst == [1, i] :
                summ += 1
print(summ)