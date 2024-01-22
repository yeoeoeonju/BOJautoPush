cols = 100
rows = 100
arr = [[0 for j in range(cols)] for i in range(rows)]


n = int(input())

for _ in range(n) :
    a, b = map(int, input().split())

    for i in range(10) :
        for j in range(10) :

            arr[a+j][b+i] += 1

count = 0

for i in range(100) :
    for j in range(100) :
        if arr[i][j] > 0 :
            count += 1

print(count)