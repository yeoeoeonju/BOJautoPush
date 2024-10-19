import numpy as np

def solution(score):
    answer = []
    fina = []
    
    for i in score :
        answer.append(np.mean(i))
    
    rank_answer = answer.copy()
    
    rank_answer.sort(reverse = True)
    
    for i in answer :
        fina.append(rank_answer.index(i)+1)
        
    return fina