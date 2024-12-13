def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    
    ch1 = a + b
    ch2 = b + a
    
    if int(ch1) > int(ch2) :
        return int(ch1)
    else :
        return int(ch2)