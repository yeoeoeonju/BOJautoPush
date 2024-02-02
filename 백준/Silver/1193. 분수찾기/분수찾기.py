N = int(input())
line = 1

while N > line :
    N -= line
    line += 1

if line % 2 != 0 :
    print(line-N+1 , '/' ,N, sep='')
else :
    print(N , '/',line-N+1, sep='')