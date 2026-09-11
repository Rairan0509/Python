def solution(myString):
    i_word =""
    for word in myString:
        if word < "l" :
            i_word += "l"
        else:
            i_word += word
    return i_word