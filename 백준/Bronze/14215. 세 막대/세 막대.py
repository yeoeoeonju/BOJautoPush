a = list(map(int, input().split()))
a.sort()


if (a[0] + a[1]) > a[2] :
    print(sum(a))
else :
    print(2 * (a[0] + a[1]) - 1 )