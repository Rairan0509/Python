def solution(rny_string: str):
    idx = rny_string.find("m")
    if idx != -1:
        return rny_string.replace(rny_string[idx], "rn")
    else:
        return rny_string