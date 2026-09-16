def solution(arr):
    X = []
    for number in arr:
        X.extend([number]*number)
    return X