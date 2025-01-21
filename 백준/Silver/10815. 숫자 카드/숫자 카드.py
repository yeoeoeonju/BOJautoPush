n = int(input())

array = set(map(int, input().split()))

m = int(input())

my_array = list(map(int, input().split()))

for i in my_array :
    
    if i in array :
        print(1, end=' ')
    else:
        print(0, end=' ')
