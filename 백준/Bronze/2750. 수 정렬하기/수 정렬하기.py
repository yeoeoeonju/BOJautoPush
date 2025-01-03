n = int(input())
lst = [0 for i in range(n)]

for i in range(n) :
    lst[i] = int(input())

lst.sort()

for i in lst:
    print(i)