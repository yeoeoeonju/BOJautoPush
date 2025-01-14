import sys

n = input()

array = []

for i in range(int(n)) :
    array.append(int(sys.stdin.readline()))
    


array.sort()

for i in array :
    print(i)