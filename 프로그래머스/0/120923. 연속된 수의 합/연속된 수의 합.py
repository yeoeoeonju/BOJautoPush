def solution(num, total):
    answer = [0 for i in range(num)]
    
    if len(answer) % 2 == 0 :
        mid = (len(answer)//2)-1
        for i in range(len(answer)) :
            answer[i] = (total // num) - mid
            mid -= 1
        
    else :
        mid = len(answer) // 2
        for i in range(len(answer)) :
            answer[i] = (total // num) - mid
            mid -= 1
        
    # num이 홀수라면 mid보다 작은 수가 num/2개, num이 짝수라면 mid보다 작은 수가 num/2-1
    return answer