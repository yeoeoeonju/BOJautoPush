def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        val = arr[i]

        rest_comb = comb(arr[i+1:], n-1)

        for cb in rest_comb:
            result.append([val] + cb)


    return result

N, M = map(int, input().split())


lst = list(map(int, input().split()))

cards = comb(lst, 3)

lst_max = []

for i in range(len(cards)) :
    summ = 0
    for j in range(len(cards[i])) :
        summ += cards[i][j]
    
    lst_max.append(summ)
    
end = []

for i in lst_max :
    if i <= M :
        end.append(i)

print(max(end))