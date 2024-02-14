n = int(input())

x_lst = []
y_lst = []

for i in range(n):
    a, b = map(int, input().split())
    x_lst.append(a)
    y_lst.append(b)

print((max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst)))