def solution(n):
    answer = []
    
    cnt = bin(n).count('1')
    
    for m in range(n+1, 1000001):
        if bin(m).count('1') == cnt :
            return m