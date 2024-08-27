def solution(number):
    answer = 0
    for i1 in range(len(number)-2):
    
        for i2 in range(i1+1, len(number)-1) :

            for i3 in range(i2+1, len(number)) :

                if number[i1] + number[i2] + number[i3] == 0 :
                    answer += 1
    return answer