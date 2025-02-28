import math

n = int(input())

array = []

for i in range(n) :
    array.append(int(input()))

array.sort()



new = []

for i in range(len(array)-1) :
    new.append(array[i+1] - array[i])


result = math.gcd(*new)


new = list(map(lambda x: (x // result) -1, new))

print(sum(new))