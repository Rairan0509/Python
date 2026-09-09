def solution(binomial):
    word_list = binomial.split()
    a = int(word_list[0])
    op = word_list[1]
    b = int(word_list[2])
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b