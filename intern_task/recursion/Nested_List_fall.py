def flat(li):
    f=[]
    if len(li)==0:
        return 0
    else:
        for i in li:
            print('this is i',i)
            if type(i)==list:
                f+=flat(i)
            else:
                f.append(i)
    return f
li=[1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(flat(li))

                
            