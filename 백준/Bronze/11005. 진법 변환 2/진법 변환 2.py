B, N = map(int, input().split())

lst = []

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while (True) :

    idx = B % N
    lst.append(alphabet[idx])
    
    B = B // N

    if B < 1 :
        break
lst.reverse()

for i in lst :
    print(i, end= '')