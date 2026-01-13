def sl(num):
    max_num=num[0]
    sl=num[0]
    for i in num:
        if i>max_num:
            sl=max_num
            max_num=i
    for i in num:
        if i>sl and i<max_num:
            sl=i
    return sl
num=[-1,-2,-3,-4,-5,-6,-3333,-3333,-333333]
print(sl(num))