n = int(input())

array = []
for i in range(n):
    array.append(list(map(str, input().split())))
    
for i in array:
    i[0] = int(i[0])
    
array.sort(key= lambda x : x[0])

for i in array:
    print(i[0], i[1])