def solution(my_string, indices):
    chars = list(my_string)
    indices = sorted(indices, reverse=True)

    for idx in indices:
        del chars[idx]

    result = "".join(chars)
    return result