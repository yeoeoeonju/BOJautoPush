def solution(n):
    answer = []
    
    for i in range(2, n+1) :
        while n % i == 0 :
            answer.append(i)
            n = n // i
    
    print(answer)
    
    answer = list(set(answer))
    answer.sort()
    return answer