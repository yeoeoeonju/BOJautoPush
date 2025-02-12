import math

array = []

t = int(input())

for i in range(t) :
    a, b = map(int, input().split())

    array.append(math.lcm(a,b))


for i in array:
    print(i)