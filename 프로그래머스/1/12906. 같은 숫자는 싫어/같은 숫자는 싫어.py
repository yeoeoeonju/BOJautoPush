def solution(arr):
    lst = [arr[0]]

    for i in range(1, len(arr)) :
        if arr[i] != arr[i-1] :
            lst.append(arr[i])
        else :
            continue

    return lst