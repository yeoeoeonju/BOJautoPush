def solution(id_pw, db):
    answer = ''
    
    for i in db :
        if i == id_pw :
            answer = 'login'
            break
        elif i[0] == id_pw[0] :
            answer = 'wrong pw'
            break
        else:
            answer = 'fail'
            
    return answer