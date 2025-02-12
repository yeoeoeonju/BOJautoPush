s = input()

answer = []

for i in range(len(s)) :
    for j in range(i, len(s)):
        answer.append(s[i:j+1])

print(len(set(answer)))
