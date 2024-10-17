
def solution(array):
    temp = []
    checked = []
    
    for i in array:
        if i not in checked :
            count_i = array.count(i)
            temp.append((i, count_i))
            checked.append(i)
            
    frequencies = [count for _, count in temp]
    
    max_freq = max(frequencies)
    
    if frequencies.count(max_freq) > 1 :
        return -1
    else :
        for num, freq in temp :
            if freq == max_freq :
                return num
    