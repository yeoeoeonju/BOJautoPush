def solution(s):
    s_lst = s.split(' ')


    for i in range(len(s_lst)) :
        new_word = ''
        for j in range(len(s_lst[i])) :

            if j % 2 == 0 :
                new_word += s_lst[i][j].upper()
            else :
                new_word += s_lst[i][j].lower()

        s_lst[i] = new_word

    return ' '.join(s_lst)
    
   