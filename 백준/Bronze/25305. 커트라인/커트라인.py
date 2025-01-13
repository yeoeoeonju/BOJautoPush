m, n = map(int, input().split())

array = list(map(int, input().split()))


array.sort(reverse=True)

print(array[n-1])
