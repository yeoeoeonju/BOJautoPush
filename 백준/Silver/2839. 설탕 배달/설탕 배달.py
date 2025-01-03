kg = int(input())

total = 0 

# n 이 5로 나눠질 수 있는 경우
# n 이 5와 3 조합으로 나눠질 수 있는 경우
# n 이 3로 나눠질 수 있는 경우
# n 이 5와 3으로 나눠질 수 없는 경우

if kg % 5 == 0 :
    print(kg // 5)  # 5로 나눠지는 경우 5, 10, 15..

else :

    while kg > 0 : # kg 가 0 이상일 때까지 계속한다
        
        kg -= 3  # 3이하의 경우로.. 이게 문제..

        total += 1 # 배달 한번 완료

        if kg % 5 == 0 : # 최대한 5kg 옮기기
            total += kg // 5
            print(total)
            break

        elif kg == 1 or kg == 2 : # 나머지 1또는 2가 남았을 때.
            print(-1)
            break

        elif kg == 0 : # kg가 3일때. 6이면 3kg, 3kg 이든 5kg 1kg 든 2번이니까..
            print(total)
            break
