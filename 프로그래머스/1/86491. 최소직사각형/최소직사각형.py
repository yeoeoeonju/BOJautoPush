def solution(sizes):
    garo = []
    sero = []

    for i in sizes :
        if i[0] < i[1]:
            temp = i[0]
            i[0] = i[1]
            i[1] = temp


        else :
            continue


    for i in range(len(sizes)) :
        garo.append(sizes[i][0])
        sero.append(sizes[i][1])

    garo.sort()
    sero.sort()

    return (garo[-1] * sero[-1])