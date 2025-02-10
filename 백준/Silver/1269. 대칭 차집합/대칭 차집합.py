import sys
input = sys.stdin.read
data = input().split()

n, m = map(int, data[:2])
a = set(map(int, data[2:2 + n]))
b = set(map(int, data[2 + n:]))

cnt = len(a - b) + len(b - a)

sys.stdout.write(str(cnt) + "\n")