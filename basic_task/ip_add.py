ip=input('enter the ip address ')
parts=ip.split('.')
if len(parts)==4:
    for p in parts:
        if not  p.isdigit():
            print('invalid ip address')
            break
    else:
        print(' your ip is valid')
else:
    print('ip is not valid')
    
