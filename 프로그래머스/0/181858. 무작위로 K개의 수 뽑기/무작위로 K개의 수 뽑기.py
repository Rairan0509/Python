def solution(arr, k = int):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
    if len(answer) < k:
        answer.extend([-1] * (k-len(answer)))
        return answer
    else:
        return answer[:k]