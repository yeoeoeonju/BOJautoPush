def solution(sides):
    answer = 0
    sides.sort(reverse=True)
    mx = sides.pop(0)
    
    if mx >= sum(sides) :
        return 2
    else :
        return 1
    