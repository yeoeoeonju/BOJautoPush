def solution(s):
   
    lst = []

    if len(s) == 4 or len(s) == 6 :

        for i in s:

            if  i in '1234567890' :
                lst.append(1)
            else :
                lst.append(0)


    if 0 in lst or len(lst) == 0 :
        return False
    else :
        return True
    