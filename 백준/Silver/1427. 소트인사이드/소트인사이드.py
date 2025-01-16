import sys

lst = sys.stdin.readline()


lst_sort = ''.join(sorted(lst, reverse=True))

print(lst_sort)