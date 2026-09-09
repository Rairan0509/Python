def solution(n_str:str):
    for idx in n_str:
        idx = 0
        if n_str[idx] == "0":
            n_str = n_str[1:]
        else:
            break
            # 0 0 1 0
            # ^ 
            # 0 1 0
            # ^
            # 1 0
            # ^
    return n_str
        # "0" 안나올때까지? idx 가져오기
        