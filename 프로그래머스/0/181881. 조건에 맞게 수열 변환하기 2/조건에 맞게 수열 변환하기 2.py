def solution(arr):
    answer = 0
    for num in arr:
        count = 0
        while True:
            if num >= 50 and num % 2 == 0:
                num = num // 2
                count += 1
            elif num < 50 and num % 2 == 1:
                num = num * 2 + 1
                count += 1
            else:
                break

        answer = max(answer, count)
    return answer