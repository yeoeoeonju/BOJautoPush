def solution(elements):
    answer = 0

    elements_2 = elements * 2

    prefix_sum = [0] * len(elements_2)
    prefix_sum[0] = elements_2[0]

    for i in range(1, len(elements_2)):
        prefix_sum[i] = prefix_sum[i-1] + elements_2[i]

    nums = set()
    for length in range(1, len(elements) + 1):
        for i in range(len(elements)):
            sum = prefix_sum[i+length] - prefix_sum[i]
            nums.add(sum)

    answer = len(nums)
    
    return answer
