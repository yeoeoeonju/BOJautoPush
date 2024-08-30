import math
def solution(arr):
    
    arr.sort()
    
    for i in range(len(arr)-1) :
        gcd = math.gcd(arr[i], arr[i+1])
        lcm = arr[i] * arr[i+1] // gcd
        arr[i+1] = lcm
        
    return lcm
    
    