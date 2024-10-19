def solution(M, N):
    answer = 0
    
    if M == 0 and N == 0 :
        return 0
    
    else :
        row = M - 1 
        col = (N - 1) * M
        
        return row + col
    