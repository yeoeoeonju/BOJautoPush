import sys

m, n = map(int, sys.stdin.readline().split())

dict = {}


for i in range(1, m+1) :
    
    a = sys.stdin.readline().rstrip()

    dict[i] = a
    dict[a] = i
    


for _ in range(n):
    
    quest = sys.stdin.readline().rstrip()

    if quest.isdigit():
        print(dict[int(quest)])

    else :
        print(dict[quest])