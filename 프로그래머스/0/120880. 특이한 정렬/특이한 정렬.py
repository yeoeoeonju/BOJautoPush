def solution(numlist, n):
    answer = []
    temp = []
    
    for i in numlist :
        temp.append(n - i)
    
    dic = {}
    
    for i in range(len(temp)):
        if temp[i] < 0 :
            
            if abs(temp[i]) not in dic:
                dic[abs(temp[i])] = [numlist[i]]
            else :
                dic[abs(temp[i])].append(numlist[i])
        else :
            if temp[i] not in dic :
                dic[temp[i]] = [numlist[i]]
            else :
                dic[temp[i]].append(numlist[i])
    
    sorted_by_key = dict(sorted(dic.items()))
    
    print(sorted_by_key)
    for i in sorted_by_key.values() :
        
        if len(i) >= 2 :
            i.sort(reverse = True)
            for j in i :
                answer.append(j)
        else :
            answer.append(i[0])
    
    return answer