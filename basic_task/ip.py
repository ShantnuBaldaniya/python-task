ip=input('enter the ip address ')
dot=0
for i in ip:
    if i=='.':
        dot+=1
if dot==3:
    print('valid ip adre')