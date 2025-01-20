import sys

n = int(sys.stdin.readline())


array = list(map(int, sys.stdin.read().strip().rstrip().split()))


    
r_array = list(set(array))

r_array.sort()



answer = {}
for i in range(len(r_array)):
    answer[r_array[i]] = i

for i in array :
    print(answer[i], end=' ')
