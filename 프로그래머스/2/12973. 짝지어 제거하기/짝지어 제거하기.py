def solution(s):
    stck = []

    for i in range(len(s)):
        """
        stck가 비어 있고 넣을 게 있으면 넣고 continue
        top이랑 현재 원소랑 비교해서 같으면 stck.pop(), 아니면 append()
        for문 다 끝나고 비어있으면 1 아니면 0
        """
        if not stck:
            stck.append(s[i])
            continue

        top = stck[-1]
        if top == s[i]:
            stck.pop()
        else:
            stck.append(s[i])

    if not stck:
        return 1
    return 0