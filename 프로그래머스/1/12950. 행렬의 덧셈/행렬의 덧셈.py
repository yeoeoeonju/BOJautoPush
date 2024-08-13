def solution(arr1, arr2):
    lst = []
    lst_answer = []

    for i in range(len(arr1)):
        for j in range(len(arr1[i])) :

            lst.append(arr1[i][j] + arr2[i][j])
        lst_answer.append(lst)
        lst = []

    return lst_answer