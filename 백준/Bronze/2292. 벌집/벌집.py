N = int(input())

house = 1
count = 1

while N > house :
    house += 6 * count
    count += 1

print(count)