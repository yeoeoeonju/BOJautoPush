T = int(input())

Q = []
D = []
N = []
P = []

for i in range(T) :
    C = int(input())
    
    Q.append(C // 25)
    
    C = C % 25

    D.append(C // 10)

    C = C % 10

    N.append(C // 5)

    C = C % 5

    P. append(C // 1)


for i in range(T) :
    print(Q[i], D[i], N[i], P[i], end = ' ')
    print()