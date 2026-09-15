def solution(picture, k):
    pixel = []

    for pic in picture:
        new_row = ""
        for i in pic:
            new_row += i*k
        pixel.extend([new_row] *k)
    
    return pixel