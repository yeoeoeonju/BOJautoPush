def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)) :
        if signs[i] == False :
            absolutes[i] = -1 * absolutes[i]
    
    answer = sum(absolutes)
    
    
    return answer