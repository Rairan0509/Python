def solution(arr, k):
    if k%2 == 0:
        r =[i+k for i in arr]
    else:
        r =[i*k for i in arr]
    return r