def solution(arr, query):
    i = 0
    for queries in query:
        if i % 2 == 0:
            arr=arr[:queries+1]
            i += 1
        else:
            arr=arr[queries:]
            i += 1
    return arr