def solution(arr, queries):
    t= 0
    for query in queries:
        t = arr[query[0]]
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = t
    return arr