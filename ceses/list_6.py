a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
b = 0
c = 0
for i in a:
    if i >0:
        b+=1
    elif i<0:
        c+=1
    else:
        pass
print("正数有{0}个,负数有{1}个".format(b,c))