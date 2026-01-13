string=input('enter the string =')
count={}
for i in string:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count)