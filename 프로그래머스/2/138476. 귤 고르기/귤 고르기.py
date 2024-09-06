def solution(k, tangerine):
    tangerine.sort()


    present = tangerine[0]
    times = []
    count = 1

    for i in range(1, len(tangerine)) :
        if present == tangerine[i] :
            count += 1
            present = tangerine[i]
        else :
            present = tangerine[i]
            times.append(count)
            count = 1
    times.append(count)



    times.sort(reverse=True)
    answer = 0





    while k >= 0 :


        for i in range(len(times)) :
            if k <= 0 :
                break

            k -= times[i]
            answer += 1

        break

    
    return answer