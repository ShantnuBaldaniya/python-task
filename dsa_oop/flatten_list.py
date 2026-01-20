def fallten_list(list1):
    result=[]
    for i in list1:
        if type(i)==list:
            for j in i:
                result.append(j)
        else:
            result.append(i)
    return result
list1=[1,[1,2,3,4],2,[2,3,3],4]
print(fallten_list(list1))