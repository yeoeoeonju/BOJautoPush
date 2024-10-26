def solution(board):
    answer = 0
    n = len(board)
    
    for y, row in enumerate(board) :
        for x, area in enumerate(row) :
            if area == 1 :
                
                for dy in [-1, 0, 1] :
                    for dx in [-1, 0, 1]:
                        
                        ny = y + dy
                        nx = x + dx
                        
                        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1 :
                            board[ny][nx] = "X"
    return sum([i.count(0) for i in board])