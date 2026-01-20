def score(dic, h=90):
    new_dic = {}
    for key, value in dic.items():  
        if value > h:
            new_dic[key] = value     
    return new_dic

dic = {}
n = int(input('enter the total pair u want: '))
for i in range(n):
    key = input('enter the student name : ')
    value = int(input('enter the score : '))
    dic[key] = value

print(score(dic, 5))
