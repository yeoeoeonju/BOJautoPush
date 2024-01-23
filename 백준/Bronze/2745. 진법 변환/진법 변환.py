N, B = map(str, input().split())

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = list(N)
B = int(B)
lst = []

for i in range(len(N)) :
        result = alphabet.index(N[i]) * (B ** (len(N)-i-1))
        lst.append(result)

print(sum(lst))