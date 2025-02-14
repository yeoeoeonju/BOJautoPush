import math

n, m = map(int, input().split())
n1, m1 = map(int, input().split())

nn = (m1 * n) + (n1 * m)
mm = m * m1

if math.gcd(nn, mm) != 1:
    print((nn // math.gcd(nn, mm)), mm // (math.gcd(nn, mm)))
else :
    print(nn, mm)