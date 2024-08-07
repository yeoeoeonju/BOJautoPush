def solution(left, right):
    lst_soo = []
    soo = 0
    max_div_num = 0
    lst_div_num =[]
    answer = 0

    for main_num in range(left, right+1):

        for div_num in range(1, main_num+1) :

            if main_num % div_num == 0 :
                soo += 1
                max_div_num = div_num

            else :
                pass

        lst_soo.append(soo)
        lst_div_num.append(max_div_num)
        soo = 0
        max_div_num = 0


    print(lst_soo)
    print(lst_div_num)

    for i in range(0, len(lst_soo)) :
        if lst_soo[i] % 2 == 0 :
            answer += lst_div_num[i]
        else :
            answer -= lst_div_num[i]

    
    
    return answer