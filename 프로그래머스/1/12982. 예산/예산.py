def solution(d, budget):
    count = 0
    d.sort()
    i = 0
    
    while budget>0 and i < len(d):
        if budget>=d[i]:
            budget-=d[i]
            i += 1
            count+=1
        else:
            break

    return count
