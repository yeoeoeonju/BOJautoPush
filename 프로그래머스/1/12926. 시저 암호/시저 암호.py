def solution(s, n):
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    down = 'abcdefghijklmnopqrstuvwxyz'

    answer = []
    for i in s :
        if i in up :
            answer.append(up[(up.index(i)+n)%26])
        elif i in down :
            answer.append(down[(down.index(i)+n)%26])
        elif i == ' ' :
            answer.append(' ')
        else :
            continue

    return (''.join(answer))