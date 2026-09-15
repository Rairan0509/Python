def solution(my_string):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ\
abcdefghijklmnopqrstuvwxyz"
    counting = []
    for i in range(52):
        counting.append(0)
        for string in my_string:
            if string == char[i]:
                counting[i] += 1
    return counting