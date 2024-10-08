def solution(array, n):
    answer = []
    temp = [abs(n-i) for i in array]
    print(temp)
    
    for i in range(len(temp)) :
        answer.append([temp[i], array[i]])
    
    answer.sort()
    
    return answer[0][1]