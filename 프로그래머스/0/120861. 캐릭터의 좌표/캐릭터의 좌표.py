def solution(keyinput, board):
    answer = [0, 0]
    
    up_down_limit = board[1] // 2
    left_right_limit = board[0] // 2
    
    for i in keyinput :
        
        if i == 'left' and answer[0] > -left_right_limit:
            answer[0] += -1
            
        elif i == 'right' and answer[0] < left_right_limit :
            answer[0] += 1
            
        elif i == 'up' and answer[1] < up_down_limit :
            answer[1] += 1
            
        elif i == 'down' and answer[1] > -up_down_limit:
            answer[1] += -1
     
        
    return answer