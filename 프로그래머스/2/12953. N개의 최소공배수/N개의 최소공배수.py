def solution(arr):
    num = 1 

    arr.sort(reverse=True)

    while True :
        temp = arr [0] * num
        count = 0

        for i in arr :
            if temp % i == 0 :
                count += 1

            else :
                break

        if count == len(arr):
            return temp

        num += 1 

    
    