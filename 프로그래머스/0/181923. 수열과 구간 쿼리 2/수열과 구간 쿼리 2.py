def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query[0], query[1], query[2]
        result = []
        for i in range(s, e+1):    
            if arr[i] > k:
                result.append(arr[i])
        if not result:
            answer.append(-1)
        else:
            answer.append(min(result))
    return answer
    