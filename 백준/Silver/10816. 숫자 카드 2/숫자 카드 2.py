n = int(input())

n_x = list(map(int, input().split()))

m = int(input())

m_x = list(map(int, input().split()))

n_dic = {}

for i in n_x:
    
    if i in n_dic:
        n_dic[i] += 1
    else :
        n_dic[i] = 1

for i in m_x :
    
    if i in n_dic:
        print(n_dic[i], end=' ')
    else :
        print(0, end=' ')