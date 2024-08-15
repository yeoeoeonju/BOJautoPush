def solution(people, limit):
    cnt = 0

    people.sort()

    people.sort(key=lambda x:-x)

    print(people)

    left = 0
    right = len(people)-1
    rest = limit

    while left <= right :
        rest -= people[left]
        left += 1

        if rest >= people[right] :
            rest -= people[right]
            right -= 1

        cnt += 1
        rest = limit

    
    return cnt