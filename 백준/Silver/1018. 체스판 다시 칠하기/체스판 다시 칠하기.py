n, m = map(int, input().split())

board = [] # 보드 만들기
result = [] # 결과 값 중 짧은 거 고를 수 있음

for i in range(n) :
    board.append(input()) # W, B 로 번갈아가면서 체스판을 만듦


for i in range(n-7) :
    for j in range(m-7): # 8x8 크기의 체스판  m-7번 판단 

        draw1 = 0
        draw2 = 0


        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B': # Black 이 아니면, white면 draw1 + 1
                        draw1 += 1 
                    else: # white 가 아니면, black이면 draw2 + 1  
                        draw2 += 1
                else :
                    if board[a][b] != 'W':
                        draw1 += 1
                    else:
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))