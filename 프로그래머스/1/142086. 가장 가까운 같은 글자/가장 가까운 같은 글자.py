def solution(s):
    check = []
    answer = []

    for i in s :
        if i not in check :
            answer.append(-1)
            check.append(i)
        else :
            check.append(i)
            temp = []
            for j in range(len(check)) :

                if check[j] == i :
                    temp.append(j)
            temp.sort(reverse=True)
            answer.append(temp[0] - temp[1])



    return answer