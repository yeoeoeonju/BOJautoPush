import math 
def solution(balls, share):
    answer = 0
    
    return math.factorial(balls) / (math.factorial(balls - share) * math.factorial(share))
    
    