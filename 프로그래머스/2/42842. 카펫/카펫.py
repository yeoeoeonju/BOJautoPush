def solution(brown, yellow):
    
    answer = []

    for i in range(1, brown + yellow+1) :
        lst = []

        if (brown + yellow) % i == 0 :
            lst.append(i)
            lst.append((brown+yellow)//i)

        else :
            continue

        answer.append(lst)

    print(answer)

    new_answer = []

    for i in range(len(answer)):
        for j in range(1) :

            if answer[i][j] >= answer[i][j+1] :
                new_answer.append(answer[i])
            else :
                continue
    for i in new_answer :
        if (i[0] - 2) * (i[1] -2) == yellow :
            return i
        else :
            continue

    
    return new_answer[0]