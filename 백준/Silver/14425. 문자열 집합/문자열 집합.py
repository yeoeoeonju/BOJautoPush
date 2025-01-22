n, m = map(int, input().split())

array = []

for i in range(n) :
    array.append(input().split())
    

test = []

for i in range(m) :
    test.append(input().split())
    
count = 0

for i in test :
    
    if i in array:
        count += 1
    else :
        continue

print(count)