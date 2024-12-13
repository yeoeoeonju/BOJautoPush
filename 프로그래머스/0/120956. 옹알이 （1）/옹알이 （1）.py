from itertools import permutations

def solution(babbling):
    answer = 0 
    check = ['aya', 'ye', 'woo', 'ma']
    
    all_check = [''.join(map(str, perm)) for r in range(1, len(check) + 1) for perm in permutations(check, r)]
    
    print(all_check)
    
    for i in babbling :
        if i in all_check :
            answer += 1
    return answer 
    
    
            
    