hex_value = input()
value = int(hex_value, 16)
for i in range(1, 16):
    print('%X'%value,'*%X'%i, '=%X'%(value*i), sep='')
